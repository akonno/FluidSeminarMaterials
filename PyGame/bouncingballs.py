# bouncingballs.py
# Copyright (c) 2025 Akihisa Konno
# MIT License (see LICENSE for details)
#
# 教材用ミニ物理エンジン（Python + pygame-ce版）
# 元: bouncingballs.js (KONNO Akihisa) をベースに移植・整理  :contentReference[oaicite:4]{index=4}
#
# 機能:
# - Ball: 位置・速度・質量・半径・色などの状態を保持
# - World: 複数Ballの時間発展(改良Euler法), 壁反射, 衝突応答, 描画サポート
# - force(): 外力モデルを差し替えるためのフック
#
# 想定の使い方（pygame側のメインループ例）:
#   world = World(width=800, height=600, restitution=0.9)
#   world.add_ball(Ball(x=100,y=100,vx=50,vy=-20,r=10,m=1))
#   ...
#   while running:
#       world.step(dt)     # 物理更新
#       world.draw(screen) # 画面に描画
#
# 学生は:
#   1. Ballを追加・削除
#   2. World.force() を書き換えて重力やバネや引力を追加
#   3. マウスクリックで新しいBallを投入
#
# 注意:
# - 座標系はpygame標準: 左上(0,0)、右+、下+。
# - 単位系は「ピクセル」「ピクセル/秒」でよいことにする。
# - step(dt)のdtは[秒]を想定 (pygameのclock.tick()から取り出したΔtなど)。

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple
import math
import pygame


@dataclass
class Ball:
    x: float
    y: float
    vx: float
    vy: float
    r: float        # 半径 [px]
    m: float        # 質量
    color: Tuple[int, int, int] = (0, 0, 0)

    def is_active(self) -> bool:
        """
        JS版では m[i] < 0 のボールは無視(死んだ扱い)としていたので、
        それを再現。:contentReference[oaicite:5]{index=5}
        """
        return self.m >= 0.0


class World:
    def __init__(self,
                 width: int,
                 height: int,
                 restitution: float = 0.9):
        """
        width, height: フィールド(=画面)サイズ [px]
        restitution: 反発係数 e
        """
        self.width = width
        self.height = height
        self.e = restitution
        self.balls: List[Ball] = []

        # 残像効果の有無
        self.trail = False  # Trueにしておくと、描画側で半透明レイヤをかぶせる等を想定

    def add_ball(self, ball: Ball):
        self.balls.append(ball)

    # ----------------------------------------------------------
    # 外力モデル
    # ----------------------------------------------------------
    def force(self,
              i: int,
              x_list: List[float],
              y_list: List[float],
              vx_list: List[float],
              vy_list: List[float]) -> Tuple[float, float]:
        """
        ball i に働く合力 (fx, fy) を返すフック関数。
        デフォルトは「重力なし・相互作用なし」→ (0,0)。

        授業ではここを学生が改造する:
          - 重力: (0, g*m)
          - バネ: -k*(x - x0), -k*(y - y0)
          - 速度比例抵抗: -c*vx, -c*vy
          - 万有引力: ほかのボールとの相互作用 etc.
        :contentReference[oaicite:6]{index=6}
        """
        # 例: 簡単な重力を入れたければ下のコメントアウトを戻す:
        # g = 200.0  # px/s^2ぐらいのスケールで好きに決める
        # m = self.balls[i].m
        # return (0.0, m*g)

        return (0.0, 0.0)

    # ----------------------------------------------------------
    # 時間発展
    # ----------------------------------------------------------
    def step(self, dt: float):
        """
        1ステップ分の時間積分を行う。
        - 改良Euler法 (Heun/modified Euler)。元のbouncingballs.jsに対応。:contentReference[oaicite:7]{index=7}
        - 壁反射
        - 衝突応答
        """
        n = len(self.balls)
        if n == 0:
            return

        # 現在の状態をリストにまとめる
        x = [b.x for b in self.balls]
        y = [b.y for b in self.balls]
        vx = [b.vx for b in self.balls]
        vy = [b.vy for b in self.balls]
        m = [b.m for b in self.balls]
        r = [b.r for b in self.balls]

        # 作業用 (予測ステップ結果)
        xd  = [0.0]*n
        yd  = [0.0]*n
        vxd = [0.0]*n
        vyd = [0.0]*n

        # --------
        # ステップ1: オイラーステップ (f1)  :contentReference[oaicite:8]{index=8}
        # --------
        f1x = [0.0]*n
        f1y = [0.0]*n
        for i in range(n):
            if m[i] < 0:
                continue
            fx, fy = self.force(i, x, y, vx, vy)
            f1x[i] = fx
            f1y[i] = fy

            xd[i]  = x[i]  + vx[i] * dt
            yd[i]  = y[i]  + vy[i] * dt
            vxd[i] = vx[i] + (fx / m[i]) * dt if m[i] != 0 else vx[i]
            vyd[i] = vy[i] + (fy / m[i]) * dt if m[i] != 0 else vy[i]

        # --------
        # ステップ2: 修正ステップ (f2)  :contentReference[oaicite:9]{index=9}
        # --------
        for i in range(n):
            if m[i] < 0:
                continue
            fx2, fy2 = self.force(i, xd, yd, vxd, vyd)

            # 改良Euler法 (平均をとる)
            # x_{t+dt} = x + 0.5*(vx + vxd)*dt
            # vx_{t+dt} = vx + 0.5*(f1 + f2)/m * dt
            new_x  = x[i]  + 0.5*(vx[i] + vxd[i]) * dt
            new_y  = y[i]  + 0.5*(vy[i] + vyd[i]) * dt
            new_vx = vx[i] + 0.5*(f1x[i] + fx2)/m[i] * dt if m[i] != 0 else vx[i]
            new_vy = vy[i] + 0.5*(f1y[i] + fy2)/m[i] * dt if m[i] != 0 else vy[i]

            x[i]  = new_x
            y[i]  = new_y
            vx[i] = new_vx
            vy[i] = new_vy

        # --------
        # 壁反射（境界条件）
        # 元JSでは「位置がはみ出し、かつ速度がその方向を向いている時だけ反転」
        # これにより高速で突き抜けた時の多重反転を抑える。:contentReference[oaicite:10]{index=10}
        # --------
        for i in range(n):
            if m[i] < 0:
                continue

            # 左右
            if (x[i] < r[i] and vx[i] < 0) or (x[i] > self.width - r[i] and vx[i] > 0):
                vx[i] = -vx[i]

            # 上下
            if (y[i] < r[i] and vy[i] < 0) or (y[i] > self.height - r[i] and vy[i] > 0):
                vy[i] = -vy[i]

        # --------
        # 衝突処理（2球間）
        # JS版と同様、「同時に2個と衝突する状況は想定しない」簡略モデル。:contentReference[oaicite:11]{index=11}
        # 手順:
        #   1. ボールi,jの中心距離dと相対速度rv = vj-viを調べる
        #   2. d < r_i + r_j かつ 互いに近づいている(dotprod < 0)時に衝突とみなす
        #   3. 接線方向は無視し、中心線方向成分だけ1次元弾性衝突(反発係数e付き)を解く
        #   4. 速度を更新
        # NOTE: JS版の式では(m[i]*lvi + m[j]*lvj ± e*m[?]*(lvj-lvi))/(m[i]+m[j])
        #       を用いていた。そこを忠実に再現する。:contentReference[oaicite:12]{index=12}
        # --------
        for i in range(n-1):
            if m[i] < 0:
                continue

            for j in range(i+1, n):
                if m[j] < 0:
                    continue

                rx = x[j] - x[i]
                ry = y[j] - y[i]
                rvx = vx[j] - vx[i]
                rvy = vy[j] - vy[i]

                d = math.hypot(rx, ry)
                # dotprod = 相対位置ベクトルと相対速度ベクトルの内積
                dotprod = rx*rvx + ry*rvy

                # 距離が離れすぎ or すでに離れる方向なら衝突していない
                if d > (r[i] + r[j]) or dotprod > 0:
                    continue

                # 正規化方向（接線じゃなく中心線方向）
                if d == 0:
                    # 同じ位置に重なったケースの保険。とりあえずスキップする。
                    continue
                nx = rx / d
                ny = ry / d

                # 両者の速度ベクトルを中心線方向に射影したスカラー成分
                lvi = vx[i]*nx + vy[i]*ny
                lvj = vx[j]*nx + vy[j]*ny

                # JS版の更新式を移植:
                # lvi2 = ( m[i]*lvi + m[j]*lvj + e*m[j]*(lvj - lvi) ) / (m[i] + m[j])
                # lvj2 = ( m[i]*lvi + m[j]*lvj - e*m[i]*(lvj - lvi) ) / (m[i] + m[j])
                # （元のJSコードはちょっと括弧が読み取りづらいが、意図としては
                #   運動量保存＋反発係数eの1次元衝突公式と一致する形）
                mi = m[i]
                mj = m[j]
                e = self.e

                # 相対速度( lvj - lvi )を使った標準形に直しておく
                lvi2 = (mi*lvi + mj*lvj + e*mj*(lvj - lvi)) / (mi + mj)
                lvj2 = (mi*lvi + mj*lvj - e*mi*(lvj - lvi)) / (mi + mj)

                # 速度ベクトルを修正（中心線方向成分だけ置き換える）
                # Δlvi = lvi2 - lvi を法線方向(nx,ny)に足す
                dvi = (lvi2 - lvi)
                dvj = (lvj2 - lvj)

                vx[i] += dvi * nx
                vy[i] += dvi * ny
                vx[j] += dvj * nx
                vy[j] += dvj * ny

        # 最終的な値をBallインスタンスに書き戻す
        for i, b in enumerate(self.balls):
            b.x  = x[i]
            b.y  = y[i]
            b.vx = vx[i]
            b.vy = vy[i]

    # ----------------------------------------------------------
    # 描画
    # ----------------------------------------------------------
    def draw(self, surface: pygame.Surface):
        """
        全てのBallを円で描画する。
        trail(残像)を実装したい場合、呼び出し側(メインループ)で
        画面の上に半透明の白をかぶせてから、draw()を呼べば
        "fadeToWhite"に近い表現になる。:contentReference[oaicite:13]{index=13}
        """
        for b in self.balls:
            if not b.is_active():
                continue
            pygame.draw.circle(
                surface,
                b.color,
                (int(b.x), int(b.y)),
                int(b.r)
            )

    def draw_trail_overlay(self, surface: pygame.Surface, alpha: int = 30):
        """
        元のfadeToWhite()は「白い半透明の四角を重ねる」ことで
        前フレームの絵をだんだん消す方式だった。:contentReference[oaicite:14]{index=14}
        pygame版では毎フレームこれを最初に呼ぶことで近い効果を再現できる。
        alpha: 0(完全透明)～255(完全不透明)
        """
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, alpha))
        surface.blit(overlay, (0, 0))
