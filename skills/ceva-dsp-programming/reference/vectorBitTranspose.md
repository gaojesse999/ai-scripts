# Bit Manipulation → Bit Transpose → Vector Bit Transpose

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Bit Transpose → Vector Bit Transpose

Vector Bit Transpose

Vector Bit Transpose
Performs bit matrix transpose operation. The matrix row size is either 32-bit or 16-bit wide.
Available Switches
byteX        The destination byte. 0 ≤ X ≤ 3
dw           Transpose bits from double-words
hi           The source part of the bits is the high part of the double words
low          The source part of the bits is the low part of the double words
w            Transpose bits from words
Intrinsic Names
vbtranspose_v32_v32_v32_dw_hi_byte0
vbtranspose_v32_v32_v32_dw_hi_byte1
vbtranspose_v32_v32_v32_dw_hi_byte2
vbtranspose_v32_v32_v32_dw_hi_byte3
vbtranspose_v32_v32_v32_dw_low_byte0
vbtranspose_v32_v32_v32_dw_low_byte1
vbtranspose_v32_v32_v32_dw_low_byte2
vbtranspose_v32_v32_v32_dw_low_byte3
vbtranspose_v32_v32_w
Instruction details in the instruction set specification
Intrinsic     vbtranspose_v32_v32_v32_dw_hi_byte0[_p]
name
Spec syntax   vbtranspose {dw, low|hi, byteX} vx[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                     Input vector operand
Operands
              3    IN3_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vbtranspose_v32_v32_v32_dw_hi_byte0_p (vIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbtranspose_v32_v32_v32_dw_hi_byte0_p version.
                   The vbtranspose_v32_v32_v32_dw_hi_byte0_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Transpose → Vector Bit Transpose
Intrinsic     vbtranspose_v32_v32_v32_dw_hi_byte1[_p]
name

Spec syntax   vbtranspose {dw, low|hi, byteX} vx[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                     Input vector operand
Operands
              3    IN3_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vbtranspose_v32_v32_v32_dw_hi_byte1_p (vIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vbtranspose_v32_v32_v32_dw_hi_byte1_p version.
                   The vbtranspose_v32_v32_v32_dw_hi_byte1_p intrinsic has different latency
                   in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Transpose → Vector Bit Transpose
Intrinsic     vbtranspose_v32_v32_v32_dw_hi_byte2[_p]
name
Spec syntax   vbtranspose {dw, low|hi, byteX} vx[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                     Input vector operand
Operands
              3    IN3_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vbtranspose_v32_v32_v32_dw_hi_byte2_p (vIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbtranspose_v32_v32_v32_dw_hi_byte2_p version.
                   The vbtranspose_v32_v32_v32_dw_hi_byte2_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When

Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Transpose → Vector Bit Transpose
Intrinsic     vbtranspose_v32_v32_v32_dw_hi_byte3[_p]
name
Spec syntax   vbtranspose {dw, low|hi, byteX} vx[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                     Input vector operand
Operands      2    IN2_V32        vec_t                     Input vector operand
              3    IN3_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vbtranspose_v32_v32_v32_dw_hi_byte3_p (vIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbtranspose_v32_v32_v32_dw_hi_byte3_p version.
                   The vbtranspose_v32_v32_v32_dw_hi_byte3_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Transpose → Vector Bit Transpose
Intrinsic     vbtranspose_v32_v32_v32_dw_low_byte0[_p]
name
Spec syntax   vbtranspose {dw, low|hi, byteX} vx[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                     Input vector operand
Operands
              3    IN3_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...

vRes1 = vbtranspose_v32_v32_v32_dw_low_byte0_p (vIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbtranspose_v32_v32_v32_dw_low_byte0_p version.
                   The vbtranspose_v32_v32_v32_dw_low_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Transpose → Vector Bit Transpose
Intrinsic     vbtranspose_v32_v32_v32_dw_low_byte1[_p]
name
Spec syntax   vbtranspose {dw, low|hi, byteX} vx[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                     Input vector operand
Operands
              3    IN3_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vbtranspose_v32_v32_v32_dw_low_byte1_p (vIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbtranspose_v32_v32_v32_dw_low_byte1_p version.
                   The vbtranspose_v32_v32_v32_dw_low_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Transpose → Vector Bit Transpose
Intrinsic     vbtranspose_v32_v32_v32_dw_low_byte2[_p]
name
Spec syntax   vbtranspose {dw, low|hi, byteX} vx[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                     Input vector operand
Operands
              3    IN3_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vbtranspose_v32_v32_v32_dw_low_byte2_p (vIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vbtranspose_v32_v32_v32_dw_low_byte2_p version.
                   The vbtranspose_v32_v32_v32_dw_low_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Transpose → Vector Bit Transpose
Intrinsic     vbtranspose_v32_v32_v32_dw_low_byte3[_p]
name
Spec syntax   vbtranspose {dw, low|hi, byteX} vx[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                     Input vector operand
              2    IN2_V32        vec_t                     Input vector operand
Operands
              3    IN3_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vbtranspose_v32_v32_v32_dw_low_byte3_p (vIn, vRes1, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbtranspose_v32_v32_v32_dw_low_byte3_p version.
                   The vbtranspose_v32_v32_v32_dw_low_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.

vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Transpose → Vector Bit Transpose
Intrinsic     vbtranspose_v32_v32_w[_p]
name
Spec syntax   vbtranspose {w} vx[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32        vec_t                        Input vector operand
Operands
              2    IN_VPR         vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbtranspose_v32_v32_w_p (vIn, vecPred);

              1.   IN_VPR last operand is relevant only for vbtranspose_v32_v32_w_p version.
                   The vbtranspose_v32_v32_w_p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
Comments           installed, 1/2 cycles are added after the generated vector instruction. The SDT
              2.
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                   the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Bit Manipulation → Bit Transpose → Vector Bit Transpose
