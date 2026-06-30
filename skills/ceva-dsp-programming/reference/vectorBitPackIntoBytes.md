# Bit Manipulation → Bit Pack → Vector Bit pack into Bytes

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Bit Pack → Vector Bit pack into Bytes

Vector Bit pack into Bytes

Vector Bit pack into Bytes
Packs a source of 8-bits into an output ranging from 1 to 7-bits wide depending on the instruction
switch.
Available Switches
kbit      Number of bits which are packed from vx[X] registers. 1 ≤ kbit ≤ 7.
Intrinsic Names
vbpackb_v32_v32_1bit
vbpackb_v32_v32_2bit
vbpackb_v32_v32_3bit
vbpackb_v32_v32_4bit
vbpackb_v32_v32_5bit
vbpackb_v32_v32_6bit
vbpackb_v32_v32_7bit
vbpackb_v32_v32
Instruction details in the instruction set specification
Intrinsic     vbpackb_v32_v32_1bit[_p]
name
Spec syntax   vbpackb {[kbit]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                       Input vector operand
Operands
              2    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbpackb_v32_v32_1bit_p (vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vbpackb_v32_v32_1bit_p version.


Main table → Bit Manipulation → Bit Pack → Vector Bit pack into Bytes
Intrinsic     vbpackb_v32_v32_2bit[_p]
name
Spec syntax   vbpackb {[kbit]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                       Input vector operand
Operands
              2    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbpackb_v32_v32_2bit_p (vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vbpackb_v32_v32_2bit_p version.


Main table → Bit Manipulation → Bit Pack → Vector Bit pack into Bytes
Intrinsic     vbpackb_v32_v32_3bit[_p]
name

Spec syntax   vbpackb {[kbit]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                       Input vector operand
Operands
              2    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbpackb_v32_v32_3bit_p (vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vbpackb_v32_v32_3bit_p version.

Main table → Bit Manipulation → Bit Pack → Vector Bit pack into Bytes
Intrinsic     vbpackb_v32_v32_4bit[_p]
name
Spec syntax   vbpackb {[kbit]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                       Input vector operand
Operands
              2    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbpackb_v32_v32_4bit_p (vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vbpackb_v32_v32_4bit_p version.


Main table → Bit Manipulation → Bit Pack → Vector Bit pack into Bytes
Intrinsic     vbpackb_v32_v32_5bit[_p]
name
Spec syntax   vbpackb {[kbit]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                       Input vector operand
Operands
              2    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbpackb_v32_v32_5bit_p (vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vbpackb_v32_v32_5bit_p version.


Main table → Bit Manipulation → Bit Pack → Vector Bit pack into Bytes
Intrinsic     vbpackb_v32_v32_6bit[_p]
name
Spec syntax   vbpackb {[kbit]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                       Input vector operand
Operands
              2    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbpackb_v32_v32_6bit_p (vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vbpackb_v32_v32_6bit_p version.


Main table → Bit Manipulation → Bit Pack → Vector Bit pack into Bytes
Intrinsic     vbpackb_v32_v32_7bit[_p]
name

Spec syntax   vbpackb {[kbit]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                       Input vector operand
Operands
              2    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbpackb_v32_v32_7bit_p (vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vbpackb_v32_v32_7bit_p version.


Main table → Bit Manipulation → Bit Pack → Vector Bit pack into Bytes
Intrinsic     vbpackb_v32_v32[_p]
name
Spec syntax   vbpackb {[kbit]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                       Input vector operand
Operands
              2    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbpackb_v32_v32_p (vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vbpackb_v32_v32_p version.


Main table → Bit Manipulation → Bit Pack → Vector Bit pack into Bytes
