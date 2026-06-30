# Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation

Vector Bit Polynomial Calculation

Vector Bit Polynomial Calculation
Performs bit polynomial calculation. The sources are 32-bit wide. The destination is 32-bit wide.
Available Switches
          Used to form the BL (Binary Line) Shift Register in differnet variations:
16bstate suitable for CRC16 and below
32bstate suitable for CRC32 and CRC24
dst       The result is written back to BL shift register vx[1]
hw        When used, high word from the source vx[X] is chosen. The default is low word.
          32bstate second phase of two-operations sequence.perfrom XOR operations on input
inxor     DW. in addition, a dedicated final XOR operation is performed between the xor'ed
          input and the rolled BL (Binary Line)
lw        When used, low word from the source vx[X] is chosen. The default is low word.

32bstate first phase of two-operations sequence. performs XOR operations on BL
roll
          (Binary Line)
xor       When used, a dedicated XOR operation is performed
Intrinsic Names
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_byte0
vbpc_v32_v32_v32_v32_v32_v32_byte1
vbpc_v32_v32_v32_v32_v32_v32_byte2
vbpc_v32_v32_v32_v32_v32_v32_byte3
vbpc_v32_v32_v32_v32_v32_v32_hh
vbpc_v32_v32_v32_v32_v32_v32_hl
vbpc_v32_v32_v32_v32_v32_v32_lh
vbpc_v32_v32_v32_v32_v32_v32_ll
vbpc_v32_v32_v32_v32_v32_v32
vbpc_v32_v32_v32_v32_v32_xor_hw
vbpc_v32_v32_v32_v32_v32_xor_lw

vbpc_v32_v32_v32_v32_v32_xor
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh

vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
vbpc_v32_v32_v32_v32_v32_v32_vi_byte0
vbpc_v32_v32_v32_v32_v32_v32_vi_byte1
vbpc_v32_v32_v32_v32_v32_v32_vi_byte2
vbpc_v32_v32_v32_v32_v32_v32_vi_byte3
vbpc_v32_v32_v32_v32_v32_v32_vi_hh
vbpc_v32_v32_v32_v32_v32_v32_vi_hl
vbpc_v32_v32_v32_v32_v32_v32_vi_lh
vbpc_v32_v32_v32_v32_v32_v32_vi_ll
vbpc_v32_v32_v32_v32_v32_v32_vi
Instruction details in the instruction set specification
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch

must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand

5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different

Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;

...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be

specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand

6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.

2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be

specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand

6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When

Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch

must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand

5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency

Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch

must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand

5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different

Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.

Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand

6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.

When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.

Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand

6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.

When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.

Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand

6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.

Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_byte0[_p]
name
Spec syntax   vbpc {[byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand
              2    IN2_V32         vec_t                     Input vector operand

3    IN3_V32         vec_t                     Input vector operand
Operands
              4    IN4_V32         vec_t                     Input vector operand
              5    IN5_V32         vec_t                     Input vector operand
              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes2 = vbpc_v32_v32_v32_v32_v32_v32_byte0_p (vIn, vIn2, vIn3, vIn4, vRes1, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_byte1[_p]
name
Spec syntax   vbpc {[byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand
              2    IN2_V32         vec_t                     Input vector operand
Operands      3    IN3_V32         vec_t                     Input vector operand
              4    IN4_V32         vec_t                     Input vector operand
              5    IN5_V32         vec_t                     Input vector operand
              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes2 = vbpc_v32_v32_v32_v32_v32_v32_byte1_p (vIn, vIn2, vIn3, vIn4, vRes1, vecPred);

                   IN_VPR last operand is relevant only for
              1.

vbpc_v32_v32_v32_v32_v32_v32_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_byte2[_p]
name
Spec syntax   vbpc {[byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand
              2    IN2_V32         vec_t                     Input vector operand
              3    IN3_V32         vec_t                     Input vector operand
Operands
              4    IN4_V32         vec_t                     Input vector operand
              5    IN5_V32         vec_t                     Input vector operand
              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes2 = vbpc_v32_v32_v32_v32_v32_v32_byte2_p (vIn, vIn2, vIn3, vIn4, vRes1, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_byte3[_p]
name

Spec syntax   vbpc {[byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand
              2    IN2_V32         vec_t                     Input vector operand
              3    IN3_V32         vec_t                     Input vector operand
Operands
              4    IN4_V32         vec_t                     Input vector operand
              5    IN5_V32         vec_t                     Input vector operand
              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes2 = vbpc_v32_v32_v32_v32_v32_v32_byte3_p (vIn, vIn2, vIn3, vIn4, vRes1, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_hh[_p]
name
Spec syntax   vbpc {[byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand
              2    IN2_V32         vec_t                     Input vector operand
              3    IN3_V32         vec_t                     Input vector operand
Operands
              4    IN4_V32         vec_t                     Input vector operand
              5    IN5_V32         vec_t                     Input vector operand
              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;

C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes2 = vbpc_v32_v32_v32_v32_v32_v32_hh_p (vIn, vIn2, vIn3, vIn4, vRes1, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_hh_p intrinsic has different latency in
Comments           case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_hl[_p]
name
Spec syntax   vbpc {[byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand
              2    IN2_V32         vec_t                     Input vector operand
              3    IN3_V32         vec_t                     Input vector operand
Operands
              4    IN4_V32         vec_t                     Input vector operand
              5    IN5_V32         vec_t                     Input vector operand
              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes2 = vbpc_v32_v32_v32_v32_v32_v32_hl_p (vIn, vIn2, vIn3, vIn4, vRes1, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_hl_p intrinsic has different latency in
Comments           case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring

correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_lh[_p]
name
Spec syntax   vbpc {[byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand
              2    IN2_V32         vec_t                     Input vector operand
              3    IN3_V32         vec_t                     Input vector operand
Operands
              4    IN4_V32         vec_t                     Input vector operand
              5    IN5_V32         vec_t                     Input vector operand
              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes2 = vbpc_v32_v32_v32_v32_v32_v32_lh_p (vIn, vIn2, vIn3, vIn4, vRes1, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_lh_p intrinsic has different latency in
Comments           case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_ll[_p]
name
Spec syntax   vbpc {[byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand
              2    IN2_V32         vec_t                     Input vector operand
              3    IN3_V32         vec_t                     Input vector operand
Operands
              4    IN4_V32         vec_t                     Input vector operand

5    IN5_V32         vec_t                     Input vector operand
              6    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes2 = vbpc_v32_v32_v32_v32_v32_v32_ll_p (vIn, vIn2, vIn3, vIn4, vRes1, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_ll_p intrinsic has different latency in
Comments           case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32[_p]
name
Spec syntax   vbpc {[byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                     Input vector operand
Operands
              2    IN2_V32         vec_t                     Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes2 = vbpc_v32_v32_v32_v32_v32_v32_p (vIn, vIn2, vIn3, vIn4, vRes1, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When

Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_xor_hw[_p]
name
Spec syntax   vbpc {xor [,lw|hw]} vx[X], vy[0], vip[0], viq[0], vir[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

              2    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              1

              3    IN2_V32         vec_t                      Input vector operand
Operands      4    IN3_V32         vec_t                      Input vector operand
              5    IN4_V32         vec_t                      Input vector operand
              6    IN5_V32         vec_t                      Input vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vIn = vbpc_v32_v32_v32_v32_v32_xor_hw_p (vIn, 0, vIn2, vIn3, vIn4, vRes, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_xor_hw_p version.
                   The vbpc_v32_v32_v32_v32_v32_xor_hw_p intrinsic has different latency in
Comments           case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_xor_lw[_p]
name
Spec syntax   vbpc {xor [,lw|hw]} vx[X], vy[0], vip[0], viq[0], vir[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

Operands      2    IN1_OFST        uint8     0..7             Offset for the first DW used from operand
                                                              1

              3    IN2_V32         vec_t                      Input vector operand
              4    IN3_V32         vec_t                      Input vector operand
              5    IN4_V32         vec_t                      Input vector operand
              6    IN5_V32         vec_t                      Input vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes;
              vprex_t vecPred;
              ...
              vIn = vbpc_v32_v32_v32_v32_v32_xor_lw_p (vIn, 0, vIn2, vIn3, vIn4, vRes, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_xor_lw_p version.
                   The vbpc_v32_v32_v32_v32_v32_xor_lw_p intrinsic has different latency in
Comments           case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_xor[_p]
name
Spec syntax   vbpc {xor [,lw|hw]} vx[X], vy[0], vip[0], viq[0], vir[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

              2    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              1

              3    IN2_V32         vec_t                      Input vector operand
Operands      4    IN3_V32         vec_t                      Input vector operand
              5    IN4_V32         vec_t                      Input vector operand

6    IN5_V32         vec_t                      Input vector operand
              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
C example     vec_t vIn4;
              vec_t vRes;
              vprex_t vecPred;
              ...
            vIn = vbpc_v32_v32_v32_v32_v32_xor_p (vIn, 0, vIn2, vIn3, vIn4, vRes, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_xor_p version.
                 The vbpc_v32_v32_v32_v32_v32_xor_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different

Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;

...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for

ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands

4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.

The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;

...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch

must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand

5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency

Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...

vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch

must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand

5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different

Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;

...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be

specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand

6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.

2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be

specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand

6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When

Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch

must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand

5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency

Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch

must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand

5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different

Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...

vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.

Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand

6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.

When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.

Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand

6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.

When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand

2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.

Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand

6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.

Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand

3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.

vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation

Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;

vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.

instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand

3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.

vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte0[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte0_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation

Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte1[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
Operands      3    IN3_V32         vec_t                      Input vector operand
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte1_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte2[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;

vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
Comments           vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p version.
              2.   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte2_p intrinsic has different
                   latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_byte3[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_byte3_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
                   When Demapper is not installed, 1/2 cycles are added after the generated
              2.

vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX
Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hh_p intrinsic has different
Comments           latency in case the Demapper block is installed/not installed on the HW.
              2.
                   When Demapper is not installed, 1/2 cycles are added after the generated
                   vector instruction. The SDT default is "Demapper installed". Therefore, for
                   ensuring correct execution on the HW, the -mno-demapper Compiler switch
                   must be specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_hl[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand

3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
              vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_hl_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
                   Demapper is not installed, 1/2 cycles are added after the generated vector
              2.
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_lh[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

              1.
                   IN_VPR last operand is relevant only for

vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_lh_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi_ll[_p]
name
Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_V32         vec_t                      Input vector operand
              3    IN3_V32         vec_t                      Input vector operand
Operands
              4    IN4_V32         vec_t                      Input vector operand
              5    IN5_V32         vec_t                      Input vector operand
              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec_t vRes1;
              vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p version.
                   The vbpc_v32_v32_v32_v32_v32_v32_vi_ll_p intrinsic has different latency
Comments           in case the Demapper block is installed/not installed on the HW. When
              2.
                   Demapper is not installed, 1/2 cycles are added after the generated vector
                   instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                   correct execution on the HW, the -mno-demapper Compiler switch must be
                   specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
Intrinsic     vbpc_v32_v32_v32_v32_v32_v32_vi[_p]
name

Spec syntax   vbpc {vi [,byteX_ll_lh_hl_hh]} vx[0], vy[0], vip[0], viq[0], vir[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
Operands
              2    IN2_V32         vec_t                      Input vector operand
            3    IN3_V32        vec_t                      Input vector operand
            4    IN4_V32        vec_t                      Input vector operand
            5    IN5_V32        vec_t                      Input vector operand
            6    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vIn3;
            vec_t vIn4;
C example   vec_t vRes1;
            vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vbpc_v32_v32_v32_v32_v32_v32_vi_p (vIn, vIn2, vIn3, vIn4, vRes2, vecPred);

                 IN_VPR last operand is relevant only for
            1.
                 vbpc_v32_v32_v32_v32_v32_v32_vi_p version.
                 The vbpc_v32_v32_v32_v32_v32_v32_vi_p intrinsic has different latency in
Comments         case the Demapper block is installed/not installed on the HW. When
                 Demapper is not installed, 1/2 cycles are added after the generated vector
            2.
                 instruction. The SDT default is "Demapper installed". Therefore, for ensuring
                 correct execution on the HW, the -mno-demapper Compiler switch must be
                 specified in case Demapper is not installed.


Main table → Bit Manipulation → Bit Polynomial Calculation → Vector Bit Polynomial
Calculation
