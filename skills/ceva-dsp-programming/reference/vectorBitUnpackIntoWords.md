# Bit Manipulation → Bit Unpack → Vector Bit Unpack into Words

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Words

Vector Bit Unpack into Words

Vector Bit Unpack into Words
Performs unpacking of modulation bits into word destinations.
Available Switches
         Number of bits which are unpacked from vx[X] registers. kbitw is either 1bit, 2bit, 4bit or
kbitw
         6bit. The default is 1bit.
Intrinsic Names
vbunpackw_v32_v32_1bit
vbunpackw_v32_v32_2bit
vbunpackw_v32_v32_4bit
vbunpackw_v32_v32_6bit
vbunpackw_v32_v32
Instruction details in the instruction set specification
Intrinsic     vbunpackw_v32_v32_1bit[_p]
name
Spec syntax   vbunpackw {[kbitw]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackw_v32_v32_1bit_p (vIn, vecPred);

                   IN_VPR last operand is relevant only for vbunpackw_v32_v32_1bit_p
Comments      1.
                   version.


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Words
Intrinsic     vbunpackw_v32_v32_2bit[_p]
name
Spec syntax   vbunpackw {[kbitw]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackw_v32_v32_2bit_p (vIn, vecPred);

                   IN_VPR last operand is relevant only for vbunpackw_v32_v32_2bit_p
Comments      1.

version.


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Words
Intrinsic     vbunpackw_v32_v32_4bit[_p]
name
Spec syntax   vbunpackw {[kbitw]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackw_v32_v32_4bit_p (vIn, vecPred);

                   IN_VPR last operand is relevant only for vbunpackw_v32_v32_4bit_p
Comments      1.
                   version.


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Words
Intrinsic     vbunpackw_v32_v32_6bit[_p]
name
Spec syntax   vbunpackw {[kbitw]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackw_v32_v32_6bit_p (vIn, vecPred);

                   IN_VPR last operand is relevant only for vbunpackw_v32_v32_6bit_p
Comments      1.
                   version.


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Words
Intrinsic     vbunpackw_v32_v32[_p]
name
Spec syntax   vbunpackw {[kbitw]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                    Input vector operand
Operands
              2    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackw_v32_v32_p (vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vbunpackw_v32_v32_p version.


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Words
