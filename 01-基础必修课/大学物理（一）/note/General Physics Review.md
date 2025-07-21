
#### **第一部分：物理学与测量 & 一维运动**

这部分内容介绍了物理学的基础单位、测量方法以及描述物体在一维空间中运动的基本概念。

* **基本物理量与单位**
    * 国际单位制 (SI) 的基本单位主要包括质量 (kg)、长度 (m) 和时间 (s)。
    * **量纲分析**: 可用于检查公式的正确性或推导物理量之间的关系。例如，在公式 $v = at^2 + bt^3$ 中，通过量纲匹配可以确定 $a$ 的单位是 $m/s^3$， $b$ 的单位是 $m/s^4$。

* **有效数字**
    * 计算结果的有效数字位数由参与运算的数字中有效数字最少或小数点后位数最少的那个决定。
        * 乘法/除法：结果的有效数字位数与操作数中有效数字最少的相同。 (例如 $3.2 \times 2.7 = 8.6$)
        * 加法/减法：结果的小数点后的位数与操作数中 小数点后位数最少的相同。 (例如 $1.513 + 27.3 = 28.8$)

* **一维运动学**
    * **位移 ($\Delta x$)**: 描述物体位置变化的矢量，定义为末位置减去初位置 $\Delta x = x_f - x_i$。
    * **平均速度 ($v_{avg}$)**: 定义为总位移除以总时间， $v_{avg} = \frac{\Delta x}{\Delta t}$。
    * **瞬时速度 ($v$)**: 物体在某一时刻的速度，定义为位置对时间的导数， $v = \frac{dx}{dt}$。
    * **平均加速度 ($a_{avg}$)**: 定义为速度变化量除以总时间， $a_{avg} = \frac{\Delta v}{\Delta t}$。
    * **瞬时加速度 ($a$)**: 物体在某一时刻的加速度，定义为速度对时间的导数， $a = \frac{dv}{dt}$。
    * **匀变速直线运动公式**:
        * $v = v_0 + at$
        * $x - x_0 = v_0t + \frac{1}{2}at^2$
        * $v^2 = v_0^2 + 2a(x-x_0)$
    * **自由落体运动**: 一种特殊的匀变速直线运动，其加速度为重力加速度 $g$。

---

#### **第二部分：矢量 & 二维和三维运动**

这部分内容将运动的描述从一维扩展到多维空间，引入了矢量的概念，并探讨了抛体运动和圆周运动。

* **矢量 (Vector)**
    * **矢量表示法**: 可以用分量形式表示，如 $\vec{A} = A_x\hat{i} + A_y\hat{j} + A_z\hat{k}$。
    * **矢量加减法**: 将矢量的对应分量相加或相减。
    * **点积 (Scalar Product)**: 结果为标量， $\vec{A} \cdot \vec{B} = A_x B_x + A_y B_y + A_z B_z = |\vec{A}||\vec{B}|\cos\theta$。 若两个非零矢量点积为0，则它们相互垂直。
    * **叉积 (Vector Product)**: 结果为矢量，其大小为 $|\vec{A} \times \vec{B}| = |\vec{A}||\vec{B}|\sin\theta$，方向由右手定则确定。
    * **矢量分解**: 可以将一个矢量分解到不同方向上，例如将矢量 $\vec{a}$ 分解到 $\vec{b}$ 的方向上，其分量大小为 $\vec{a} \cdot \hat{b}$。

* **二维和三维运动**
    * **位置、速度和加速度**: 均用矢量表示。
        * 平均速度: $\vec{v}_{avg} = \frac{\Delta \vec{r}}{\Delta t}$
        * 瞬时速度: $\vec{v} = \frac{d\vec{r}}{dt}$
        * 瞬时加速度: $\vec{a} = \frac{d\vec{v}}{dt}$
    * **抛体运动 (Projectile Motion)**:
        * 可分解为水平方向的匀速直线运动 ($a_x = 0$) 和竖直方向的匀变速直线运动 ($a_y = -g$) 。
        * 水平射程: $R = \frac{v_0^2 \sin(2\theta_0)}{g}$，当抛射角为 $45^\circ$ 时，射程最远。
    * **匀速圆周运动 (Uniform Circular Motion)**:
        * 速度大小恒定，但方向不断变化。
        * 存在一个指向圆心的向心加速度: $a_c = \frac{v^2}{R}$。
    * **相对运动 (Relative Motion)**:
        * 速度合成公式: $\vec{v}_{pg} = \vec{v}_{pa} + \vec{v}_{ag}$ (物体p相对于地面g的速度 = 物体p相对于介质a的速度 + 介质a相对于地面g的速度)。

---

#### **第三部分：力与运动**

这部分内容介绍了力的基本概念、牛顿三大定律，以及摩擦力、圆周运动动力学等具体应用。

* **牛顿定律**
    * **牛顿第二定律**: 物体的加速度与所受的合外力成正比，与质量成反比。数学表达式为 $\sum \vec{F} = m\vec{a}$。 这是解决动力学问题的核心。
    * **惯性 (Inertia)**: 物体保持其运动状态不变的性质。例如，猛拉悬挂重球的下绳，由于球的惯性，下绳先断。

* **常见力及其应用**
    * **重力 ($F_g$)**: $F_g = mg$。
    * **支持力 (Normal Force, $N$)**: 由表面提供，方向垂直于表面。当物体在水平面上受斜向下的力时，$N = mg + F\sin\theta$。 当受斜向上的力时，$N = mg - P\sin\theta$。
    * **摩擦力 (Friction)**:
        * **静摩擦力 ($f_s$)**: 阻止物体开始运动的力，其大小可变， $f_s \le \mu_s N$。
        * **动摩擦力 ($f_k$)**: 物体运动时受到的摩擦力，大小恒定， $f_k = \mu_k N$。 通常 $f_k < f_{s, max}$。
    * **张力 (Tension, $T$)**: 绳子或线缆施加的拉力。

* **动力学应用**
    * **连接体问题**: 将多个物体视为一个系统，或隔离单个物体进行受力分析来求解加速度和内力。
    * **斜面上的运动**: 通常将力分解到平行于斜面和垂直于斜面的方向上。
    * **圆周运动动力学**:
        * 物体做圆周运动所需的向心力由一个或多个力的合力提供， $\sum F_{radial} = m \frac{v^2}{R}$。
        * **道路倾斜**: 倾斜角度 $\theta$ 满足 $\tan\theta = \frac{v^2}{gR}$ 时，可以仅靠支持力提供向心力，无需摩擦力。
    * **空气阻力与终端速度**:
        * 当空气阻力 ($f_{air}$，通常与速度v的幂成正比，如 $f_{air} = kv$) 与重力大小相等时，物体加速度为零，达到终端速度 ($v_{terminal}$) 。
        * 从 $a = g - kv$ 出发，可以推导出速度随时间变化的公式 $v(t) = \frac{g}{k}(1-e^{-kt})$，终端速度为 $v_{terminal} = \frac{g}{k}$。
## 功、能、功率

这部分主要围绕能量守恒这一核心思想，探讨了功、动能、势能及其转化。

### 1. 功 (Work)
* **恒力做功**: 如果一个恒力 $\vec{F}$ 作用在物体上，使物体发生位移 $\vec{d}$，则该力所做的功为：
    $$
    W = \vec{F} \cdot \vec{d} = Fd\cos\theta
    $$
    其中 $\theta$ 是力与位移方向的夹角。
* **变力做功**: 如果力是变化的，需要通过积分计算：
    $$
    W = \int_{A}^{B} \vec{F} \cdot d\vec{s}
    $$
    在处理一维问题时，可以通过 $F-x$ 图线下的面积来计算功。

### 2. 动能和动能定理 (Kinetic Energy and Work-Kinetic Energy Theorem)
* **动能**: 物体由于运动而具有的能量，其大小为：
    $$
    K = \frac{1}{2}mv^2
    $$
* **动能定理**: 合外力对物体所做的总功等于物体动能的变化量。这是一个普适的定理，适用于所有情况。
    $$
    W_{net} = \Delta K = K_f - K_i = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2
    $$

### 3. 功率 (Power)
* **平均功率**: 单位时间内所做的功。
    $$
    P_{avg} = \frac{W}{\Delta t}
    $$
* **瞬时功率**: 力 $\vec{F}$ 在物体速度为 $\vec{v}$ 时的瞬时功率为：
    $$
    P = \frac{dW}{dt} = \vec{F} \cdot \vec{v}
    $$

### 4. 势能和保守力 (Potential Energy and Conservative Forces)
* **保守力**: 做功与路径无关，仅取决于始末位置的力（如重力、弹簧弹力）。
* **势能**: 与物体在场中的位置相关的能量。势能的变化量定义为保守力做功的负值：
    $$
    \Delta U = U_f - U_i = -W_c
    $$
* **从势能求力**: 在一维情况下，保守力是势能函数对位置导数的负值：
    $$
    F(x) = -\frac{dU(x)}{dx}
    $$
* **常见势能**:
    * 重力势能: $U_g = mgh$ (通常选择地面为零势能点)
    * 弹簧势能: $U_s = \frac{1}{2}kx^2$ (x为弹簧的伸长量或压缩量)

### 5. 机械能守恒定律 (Conservation of Mechanical Energy)
* **机械能**: 系统的动能与势能之和，$E_{mech} = K + U$。
* **守恒条件**: 如果一个系统中只有保守力做功（或者非保守力做的总功为零），则系统的总机械能保持不变。
    $$
    \Delta E_{mech} = \Delta K + \Delta U = 0 \quad \Rightarrow \quad K_i + U_i = K_f + U_f
    $$
* **非保守力做功**: 如果有摩擦力等非保守力 $f$ 做功，则系统的机械能会发生变化，其变化量等于非保守力做的功：
    $$
    W_{nc} = \Delta E_{mech}
    $$

### 6. 势能图与平衡 (Potential Energy Curve and Equilibrium)
* 从 $U-x$ 图像可以分析物体的运动和受力情况。
* **平衡点**: 受合力为零的点，即 $F(x) = -\frac{dU}{dx} = 0$，对应势能曲线的极值点或平坦部分。
    * **稳定平衡**: 势能的极小值点。
    * **不稳定平衡**: 势能的极大值点。
    * **中性平衡 (随遇平衡)**: 势能为常数的区域（曲线是水平直线）。

---

## 动量、冲量和碰撞

这部分研究物体的动量变化与守恒，特别是在碰撞和爆炸等短暂相互作用中。

### 1. 质心 (Center of Mass)
* **质心坐标**: 对于一个粒子系统，其质心坐标为：
    $$
    x_{com} = \frac{\sum m_i x_i}{\sum m_i}, \quad y_{com} = \frac{\sum m_i y_i}{\sum m_i}, \quad z_{com} = \frac{\sum m_i z_i}{\sum m_i}
    $$
* **质心运动**: 质心的运动只与系统的总质量和所受的合外力有关，其行为如同一个质量等于系统总质量、受力等于系统所受合外力的质点。
    $$
    \vec{F}_{net, ext} = M_{total} \vec{a}_{com}
    $$

### 2. 线性动量和动量守恒 (Linear Momentum and Its Conservation)
* **动量**: 物体质量与速度的乘积，是矢量。
    $$
    \vec{p} = m\vec{v}
    $$
* **牛顿第二定律的动量形式**: 作用在物体上的净外力等于其动量随时间的变化率。
    $$
    \vec{F}_{net} = \frac{d\vec{p}}{dt}
    $$
* **动量守恒定律**: 如果一个系统所受的合外力为零，那么该系统的总动量保持不变。这是自然界最基本的守恒定律之一。
    $$
    \vec{P}_{total} = \sum \vec{p}_i = \text{常数} \quad \Rightarrow \quad \vec{P}_{initial} = \vec{P}_{final}
    $$

### 3. 冲量 (Impulse)
* **定义**: 力在一段时间上的积累效应，是矢量。
    $$
    \vec{J} = \int_{t_i}^{t_f} \vec{F}(t) dt
    $$
* **冲量-动量定理**: 物体所受的净冲量等于其动量的变化量。
    $$
    \vec{J}_{net} = \Delta \vec{p} = \vec{p}_f - \vec{p}_i
    $$

### 4. 碰撞 (Collisions)
* **共同点**: 在所有碰撞中，如果没有外部冲力，系统的总动量都是守恒的。
* **弹性碰撞 (Elastic Collision)**: 碰撞前后系统的总动能不变。动量和动能都守恒。
* **非弹性碰撞 (Inelastic Collision)**: 碰撞前后系统的总动能不守恒（通常是减少）。只有动量守恒。
* **完全非弹性碰撞 (Perfectly Inelastic Collision)**: 碰撞后物体粘在一起，以共同的速度运动。动能损失最大，但动量依然守恒。

### 5. 变质量系统 (Variable-Mass Systems)
* 例如火箭发射，通过向后喷射气体获得向前的推力。这类问题本质上也是动量守恒的应用。

---

## 旋转运动

这部分将线性运动的概念（位移、速度、力、动量等）推广到旋转领域。

### 1. 旋转运动学 (Rotational Kinematics)
* **角位置、角速度、角加速度**:
    * 角位置: $\theta$ (rad)
    * 角速度: $\omega = \frac{d\theta}{dt}$ (rad/s)
    * 角加速度: $\alpha = \frac{d\omega}{dt}$ (rad/s²)
* **匀角加速度运动公式**:
    * $\omega = \omega_0 + \alpha t$
    * $\theta - \theta_0 = \omega_0 t + \frac{1}{2}\alpha t^2$
    * $\omega^2 = \omega_0^2 + 2\alpha(\theta - \theta_0)$
* **线量与角量的关系**:
    * 弧长: $s = r\theta$
    * 切向速度: $v_t = r\omega$
    * 切向加速度: $a_t = r\alpha$
    * 径向(向心)加速度: $a_r = \frac{v_t^2}{r} = \omega^2 r$

### 2. 转动惯量和转动动能 (Rotational Inertia and Kinetic Energy)
* **转动惯量 (I)**: 衡量物体转动惯性大小的物理量，取决于质量分布和转轴位置。
    $$
    I = \sum m_i r_i^2 \quad \text{(对于质点系)} \quad \text{或} \quad I = \int r^2 dm \quad \text{(对于连续体)}
    $$
* **转动动能**:
    $$
    K_{rot} = \frac{1}{2}I\omega^2
    $$

### 3. 力矩和牛顿第二定律的转动形式 (Torque and Newton's Second Law for Rotation)
* **力矩 ($\tau$)**: 描述力使物体转动效果的物理量，是矢量。
    $$
    \vec{\tau} = \vec{r} \times \vec{F}
    $$
    其大小为 $\tau = rF\sin\phi$，其中 $\phi$ 是 $\vec{r}$ 和 $\vec{F}$ 的夹角。
* **牛顿第二定律的转动形式**: 作用在刚体上的净外力矩等于其转动惯量与角加速度的乘积。
    $$
    \sum \vec{\tau}_{net} = I\vec{\alpha}
    $$

### 4. 角动量 (Angular Momentum)
* **质点的角动量**:
    $$
    \vec{l} = \vec{r} \times \vec{p} = \vec{r} \times (m\vec{v})
    $$
* **刚体的角动量**:
    $$
    \vec{L} = I\vec{\omega}
    $$
* **力矩与角动量的关系**: 净外力矩等于角动量对时间的变化率。
    $$
    \vec{\tau}_{net} = \frac{d\vec{L}}{dt}
    $$
* **角动量守恒定律**: 如果一个系统所受的净外力矩为零，则该系统的总角动量保持不变。
    $$
    I_i \omega_i = I_f \omega_f
    $$

### 5. 滚动 (Rolling Motion)
* **纯滚动**: 滚动与滑动的结合，轮子与地面接触点无相对滑动。
* **纯滚动的条件**: 质心速度 $v_{com}$ 与角速度 $\omega$ 满足 $v_{com} = R\omega$。
* **滚动动能**: 滚动物体的总动能是平动动能和转动动能之和。
    $$
    K_{rolling} = K_{trans} + K_{rot} = \frac{1}{2}Mv_{com}^2 + \frac{1}{2}I_{com}\omega^2
    $$

---

## 振动

这部分主要研究在平衡位置附近的周期性往复运动，特别是简谐振动。

### 1. 简谐振动 (Simple Harmonic Motion, SHM)
* **定义**: 物体所受回复力 $F$ 与其偏离平衡位置的位移 $x$ 成正比且方向相反的运动 ($F = -kx$)。
* **运动方程**:
    $$
    x(t) = x_m \cos(\omega t + \phi)
    $$
    其中，$x_m$ 是振幅，$\omega$ 是角频率，$\phi$ 是初相位。
* **速度和加速度**:
    $$
    v(t) = -\omega x_m \sin(\omega t + \phi)
    $$
    $$
    a(t) = -\omega^2 x_m \cos(\omega t + \phi) = -\omega^2 x
    $$
* **角频率、周期和频率**:
    * 弹簧振子: $\omega = \sqrt{\frac{k}{m}}$
    * 周期: $T = \frac{2\pi}{\omega} = \frac{1}{f}$

### 2. 简谐振动的能量 (Energy in SHM)
* 系统的总机械能守恒，且等于最大动能或最大势能。
    $$
    E = K + U = \frac{1}{2}mv^2 + \frac{1}{2}kx^2 = \frac{1}{2}kx_m^2 = \frac{1}{2}mv_{max}^2 = \text{常数}
    $$
* 在振动过程中，动能和势能相互转化。
    * 在平衡位置($x=0$)，动能最大，势能为零。
    * 在最大位移处($x=\pm x_m$)，势能最大，动能为零。

### 3. 摆 (Pendulums)
* **单摆 (Simple Pendulum)**: 在小角度近似下 ($\theta$ 很小) 进行简谐振动。
    $$
    T = 2\pi\sqrt{\frac{L}{g}} \quad (\omega = \sqrt{\frac{g}{L}})
    $$
* **物理摆 (Physical Pendulum)**: 任何绕固定轴摆动的刚体。
    $$
    T = 2\pi\sqrt{\frac{I}{mgh}}
    $$
    其中 $I$ 是绕转轴的转动惯量，$h$ 是转轴到质心的距离。
* **扭摆 (Torsion Pendulum)**:
    $$
    T = 2\pi\sqrt{\frac{I}{\kappa}}
    $$
    其中 $\kappa$ 是悬丝的扭转系数。

### 4. 阻尼振动 (Damped Harmonic Motion)
* 由于存在阻尼力（如空气阻力），振动的振幅会随时间减小。
* 其运动方程通常表示为：
    $$
    x(t) = x_m e^{-bt/2m} \cos(\omega' t + \phi)
    $$
    其中 $b$ 是阻尼系数，$\omega'$ 是阻尼振动的角频率。
## 机械波与声波

### 1. 波的基本描述
- **波动方程**: 正弦行波的数学表达式为 $y(x,t) = y_m \sin(kx \pm \omega t + \phi)$。
    - $y_m$: 振幅 (Amplitude)
    - $k$: 角波数 (Angular wave number), $k = 2\pi/\lambda$
    - $\omega$: 角频率 (Angular frequency), $\omega = 2\pi/T = 2\pi f$
    - $\phi$: 相位常数 (Phase constant), 由初始条件 (如 $t=0, x=0$ 处的位移和速度) 决定。
    - '$-$' 号表示波沿 x 轴正向传播，'$+$' 号表示波沿 x 轴负向传播。
- **波速 (Wave Speed)**: 波速 $v$ 与角频率 $\omega$ 和角波数 $k$ 的关系为 $v = \omega/k = \lambda f$。
- **质点振动速度**: 绳子上某点的横向振动速度为 $u(x,t) = \frac{\partial y}{\partial t}$。其方向取决于该点在波形上的位置和波的传播方向。

### 2. 弦上的波
- **线密度 (Linear Mass Density)**: 定义为单位长度的质量, $\mu = m/L$。
- **弦波波速**: 弦上传播的横波速度由弦的张力 $\tau$ (或 $T_s$) 和线密度 $\mu$ 决定: $v = \sqrt{\frac{\tau}{\mu}}$。
- **波的能量**:
    - **平均功率**: 正弦波在弦上传播的平均能量传输速率（功率）为 $P_{avg} = \frac{1}{2}\mu v \omega^2 y_m^2$。

### 3. 波的叠加与干涉
- **叠加原理 (Superposition Principle)**: 当两列或多列波在同一介质中相遇时，总位移是各列波单独位移的矢量和。
- **干涉 (Interference)**:
    - **相干条件**: 两列波频率相同、相位差恒定。
    - **相长干涉 (Constructive)**: 相位差 $\Delta\phi$ 为 $2n\pi$ ($n=0, 1, 2, ...$)，或波程差 $\Delta r$ 为 $\lambda$ 的整数倍。合成振幅最大。
    - **相消干涉 (Destructive)**: 相位差 $\Delta\phi$ 为 $(2n+1)\pi$ ($n=0, 1, 2, ...$)，或波程差 $\Delta r$ 为半波长的奇数倍。合成振幅最小。
- **合成波振幅**: 两列振幅均为 $A$ 的波干涉后，合成振幅为 $A_{res} = |2A \cos(\frac{\Delta\phi}{2})|$。

### 4. 驻波与共振
- **驻波 (Standing Waves)**: 由两列振幅、波长、频率相同，但传播方向相反的波叠加而成。
- **波节 (Nodes)**: 始终保持静止的点，相邻波节间距为 $\lambda/2$。
- **波腹 (Antinodes)**: 振幅最大的点，相邻波腹间距也为 $\lambda/2$。
- **弦的共振频率**: 两端固定的弦上形成驻波的条件是弦长 L 为半波长的整数倍，即 $L = n\frac{\lambda}{2}$。对应的共振频率为：
    $$ f_n = \frac{nv}{2L} = \frac{n}{2L}\sqrt{\frac{\tau}{\mu}} \quad (n=1, 2, 3, ...) $$
    - $n=1$ 为基频（第一谐波），$n>1$ 为谐波。

### 5. 声波
- **位移振幅与压强振幅**: 声波中的位移和压强变化是相互关联的，但它们的相位-相差 $\pi/2$。
- **声强级 (Sound Intensity Level)**: 用分贝 (dB) 表示，定义为 $\beta = (10 \text{ dB}) \log\frac{I}{I_0}$，其中参考声强 $I_0 = 10^{-12} W/m^2$。
- **节拍 (Beats)**: 两个频率相近 ($f_1$ 和 $f_2$) 的声源叠加时，会听到强弱周期性变化的现象，拍频为 $f_{beat} = |f_1 - f_2|$。
- **多普勒效应 (Doppler Effect)**: 当波源(S)和探测器(D)相对于介质运动时，探测器接收到的频率 $f'$ 不同于波源发出的频率 $f$。
    $$ f' = f \left(\frac{v \pm v_D}{v \mp v_S}\right) $$
    - $v$: 声速, $v_D$: 探测器速度, $v_S$: 波源速度。
    - 速度方向规则: 当探测器向波源运动时 $v_D$ 取正号，反之取负号；当波源向探测器运动时 $v_S$ 取负号，反之取正号。
    - **有风情况**: 需要转换到以空气为静止的参考系来计算。
- **激波 (Shock Waves)**: 当波源速度 $v_S$ 超过介质中的波速 $v$ 时形成。激波（马赫锥）的半顶角 $\theta$ 满足 $\sin\theta = v/v_S$。

---

## 热力学第一定律

### 1. 温度与热力学第零定律
- **热力学第零定律 (Zeroth Law of Thermodynamics)**: 如果物体 A 和 B 分别与物体 C 处于热平衡状态，那么 A 和 B 也彼此处于热平衡状态。
- **温标 (Temperature Scales)**:
    - 摄氏度 ($^\circ C$) 和开尔文 (K) 的关系: $T_K = T_C + 273.15$。
    - 摄氏度和开尔文温标的“1度”大小相同，即 $\Delta T_K = \Delta T_C$。

### 2. 热膨胀 (未在题目中直接考察，但为本章基础)

### 3. 热量与内能
- **热容量 (Heat Capacity)**: 物体温度改变1K所吸收或放出的热量, $C = Q/\Delta T$。
- **内能 (Internal Energy)**: 系统内所有粒子动能和势能的总和，是状态函数，其变化量 $\Delta E_{int}$ 只与初末状态有关，与过程路径无关。

### 4. 热力学第一定律 (First Law of Thermodynamics)
- **定律表述**: 系统内能的变化量等于系统吸收的热量减去系统对外做的功。
    $$ \Delta E_{int} = Q - W $$
    - $Q$: 系统吸收的热量 ($Q>0$ 吸热, $Q<0$ 放热)。
    - $W$: 系统对外做的功 ($W>0$ 对外做功, $W<0$ 外界对系统做功)。
- **P-V 图与功**:
    - 气体对外做的功 $W = \int p dV$，在 P-V 图上等于过程曲线下的面积。
    - **循环过程 (Cyclic Process)**: 系统回到初始状态，$\Delta E_{int} = 0$。因此 $Q = W$，即一个循环中净吸收的热量等于净对外做的功（P-V图闭合曲线包围的面积）。

### 5. 特殊热力学过程
- **绝热过程 (Adiabatic Process)**: 系统与外界没有热量交换, $Q=0$。因此 $\Delta E_{int} = -W$。
- **等容过程 (Isochoric Process)**: 体积不变, $\Delta V=0$。因此系统不做功, $W=0$。所以 $\Delta E_{int} = Q$。
- **等压过程 (Isobaric Process)**: 压强不变。做功 $W = p \Delta V$。
- **等温过程 (Isothermal Process)**: 温度不变。对于理想气体，$\Delta E_{int} = 0$。因此 $Q = W$。
- **自由膨胀 (Free Expansion)**: 对真空的绝热膨胀。$Q=0, W=0$，因此 $\Delta E_{int}=0$。

### 6. 热传递机制
- **热传导 (Conduction)**: 导热速率满足 $P_{cond} = kA \frac{T_H - T_L}{L}$。
    - $k$: 热导率 (Thermal conductivity)。
- **热阻 (Thermal Resistance)**: R值定义为 $R=L/k$。R值越大，隔热效果越好。
- **热辐射 (Radiation)**: 物体以电磁波形式辐射能量的速率为 $P_{rad} = \sigma \epsilon A T^4$。
    - $\sigma$: 斯特藩-玻尔兹曼常数。
    - $\epsilon$: 发射率 (Emissivity)。
    - $T$: 绝对温度 (Kelvin)。

---

## 气体动理论

### 1. 理想气体
- **理想气体状态方程**: $pV = nRT$ 或 $pV = NkT$。
    - $n$: 摩尔数, $R$: 普适气体常数。（宏观状态）
    - $N$: 分子数, $k$: 玻尔兹曼常数。（微观状态）

### 2. 压强、温度与速度
- **压强微观公式**: $p = \frac{nM v_{rms}^2}{3V}$。
- **分子平均平动动能**: $\overline{K} = \frac{1}{2}m\overline{v^2} = \frac{3}{2}kT$。只与绝对温度有关。
- **方均根速率 (Root-mean-square speed)**: $v_{rms} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3kT}{m}}$。
- **平均速率 (Average speed)**: $v_{avg} = \sqrt{\frac{8RT}{\pi M}}$。
- **最概然速率 (Most probable speed)**: $v_p = \sqrt{\frac{2RT}{M}}$。
- **速率关系**: $v_p < v_{avg} < v_{rms}$。

### 3. 气体分子热运动
- **平均自由程 (Mean Free Path)**: 分子两次连续碰撞之间平均走过的距离 $\lambda = \frac{1}{\sqrt{2}\pi d^2 (N/V)}$。
- **碰撞频率 (Collision Rate)**: 单位时间内一个分子发生的平均碰撞次数 $f_{collision} = \frac{v_{avg}}{\lambda}$。

### 4. 理想气体内能与摩尔热容
- **内能 (Internal Energy)**: 理想气体的内能只与温度有关, $E_{int} = n(\frac{f}{2})RT$。
    - $f$: 自由度 (degrees of freedom)。
    - 单原子气体 (Monatomic): $f=3$。
    - 双原子气体 (Diatomic, 考虑转动): $f=5$。
    - 多原子气体 (Polyatomic, 考虑转动): $f=6$。
- **摩尔定容热容 (Molar specific heat at constant volume)**: $C_V = (\frac{f}{2})R$。
- **摩尔定压热容 (Molar specific heat at constant pressure)**: $C_p = C_V + R$。
- **内能变化**: $\Delta E_{int} = nC_V\Delta T$。
- **定压过程吸热**: $Q = nC_p\Delta T$。
- **绝热过程方程**: 对于理想气体，$pV^\gamma = \text{常数}$ and $TV^{\gamma-1} = \text{常数}$。
    - $\gamma = C_p/C_V$ (绝热指数)。

### 5. 不同过程的功
- **压缩过程做功**: 将气体从 $V_i$ 压缩到 $V_f$，外界需要做的功为 $W_{ext} = -W = \int_{V_i}^{V_f} p dV$。对于相同的体积变化，绝热过程曲线最陡峭，做的功最多；其次是等温过程；等压过程做的功最少。

---

## 熵与热力学第二定律

### 1. 不可逆过程与熵
- **热力学第二定律 (Second Law of Thermodynamics)**:
    - **开尔文表述**: 不可能制造出一种循环工作的热机，只从单一热源吸热，将之完全变为功，而不产生其他任何影响。
    - **克劳修斯表述**: 不可能把热量从低温物体传到高温物体而不引起其它变化。
- **熵 (Entropy)**: 度量系统无序程度的物理量，是状态函数。
    - **宏观定义**: 对于可逆过程，熵变 $dS = \frac{dQ}{T}$。
    - **微观定义 (Boltzmann's entropy formula)**: $S = k \ln W$，其中 $W$ 是宏观态对应的微观态数目（多重性）。
- **熵增原理**: 在一个孤立系统中，熵永不减少。$\Delta S \ge 0$。
    - 对于可逆过程，$\Delta S = 0$。
    - 对于不可逆过程，$\Delta S > 0$。

### 2. 熵变的计算
- **理想气体熵变**: $\Delta S = nC_V \ln(T_f/T_i) + nR \ln(V_f/V_i)$。
- **等温过程**: $\Delta T=0$, $\Delta S = nR \ln(V_f/V_i)$。
- **等压过程**: $\Delta S = nC_p \ln(T_f/T_i)$。
- **可逆绝热过程**: $dQ=0$, $\Delta S = 0$ (等熵过程)。
- **自由膨胀**: 不可逆过程，虽然$Q=0$，但熵增加。
- **热传导**: 热量从高温物体传向低温物体，总熵增加。

### 3. 热机 (Heat Engines)
- **热机**: 在两个热源之间循环工作，将部分热量转化为功的装置。
- **效率 (Efficiency)**: $\epsilon = \frac{W}{|Q_H|} = \frac{|Q_H| - |Q_L|}{|Q_H|} = 1 - \frac{|Q_L|}{|Q_H|}$。
    - $W$: 净功, $Q_H$: 从高温热源吸收的热量, $Q_L$: 向低温热源放出的热量。

### 4. 制冷机 (Refrigerators)
- **制冷机**: 消耗功，把热量从低温物体转移到高温物体的装置。
- **制冷系数 (Coefficient of Performance, COP)**: $K = \frac{|Q_L|}{|W|} = \frac{|Q_L|}{|Q_H| - |Q_L|}$。

### 5. 卡诺循环 (Carnot Cycle)
- **卡诺热机**: 在两个给定温度的热源之间工作的效率最高的可逆热机。
- **卡诺效率**: $\epsilon_C = 1 - \frac{T_L}{T_H}$ (温度为绝对温标)。
- **卡诺制冷系数**: $K_C = \frac{T_L}{T_H - T_L}$。
- **卡诺定理**: 任何工作在两个给定温度热源之间的实际热机，其效率都不能超过卡诺热机的效率。$\epsilon_{real} \le \epsilon_C$。

### 6. 统计力学初步
- **微观态 (Microstates)**: 系统中每个粒子的具体状态。
- **宏观态 (Macrostates)**: 由宏观物理量（如P, V, T）描述的状态。
- **多重性 (Multiplicity)**: 一个宏观态所对应的微观态的数目 $W$。
- **组合计算**: 将 N 个粒子分配到两个容器中的多重性为 $W = \frac{N!}{n_1! n_2!}$，其中 $n_1+n_2=N$。最可能出现的宏观态是多重性最大的态（通常是分布最均匀的态）。