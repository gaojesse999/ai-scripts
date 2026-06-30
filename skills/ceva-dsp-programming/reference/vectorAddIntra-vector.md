# Intra Vector → Add Intra-Vector → Vector Add Intra-Vector

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Intra Vector → Add Intra-Vector → Vector Add Intra-Vector

Vector Add Intra-Vector

Vector Add Intra-Vector
Performs intra-vector addition between sources that are located in the same vector. Each source
is 32-bit wide. The destination is 32-bit wide or 40-bit wide determined by the vector register
type.
Available Switches
          Number of atomic operations. An atomic operation is defined as adding a single register.
Oop
          1op ≤ Oop ≤ 8op
s         Saturation switch.
Intrinsic Names
vaddint_v32_v40_p_4p
vaddint_v32_v40_s_p_4p
vaddint_v32_v32_s_p_4p
vaddint_v32_v32_p_4p
Instruction details in the instruction set specification
Intrinsic     vaddint_v32_v40_p_4p
name
Spec syntax   vaddint {Oop [,s_sw]} vx[0], voz[Z], ?vprX

Return type   vec40_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

Operands                                                      Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                              result operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vaddint_v32_v40_p_4p (8, vIn, 0, vecPred);

                   The vaddint_v32_v40_p_4p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
Comments      1.
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                   the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Intra Vector → Add Intra-Vector → Vector Add Intra-Vector
Intrinsic     vaddint_v32_v40_s_p_4p
name
Spec syntax   vaddint {Oop [,s_sw]} vx[0], voz[Z], ?vprX

Return type   vec40_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands                                                      Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                              result operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vaddint_v32_v40_s_p_4p (8, vIn, 0, vecPred);

                   The vaddint_v32_v40_s_p_4p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
Comments      1.
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                the HW, the -mno-demapper Compiler switch must be specified in case
                Demapper is not installed.


Main table → Intra Vector → Add Intra-Vector → Vector Add Intra-Vector
Intrinsic     vaddint_v32_v32_s_p_4p
name

Spec syntax   vaddint {Oop, s} vx[0], viz[Z], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands                                                      Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                              result operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vaddint_v32_v32_s_p_4p (8, vIn, 0, vecPred);

                   The vaddint_v32_v32_s_p_4p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
Comments      1.
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                   the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Intra Vector → Add Intra-Vector → Vector Add Intra-Vector
Intrinsic     vaddint_v32_v32_p_4p
name
Spec syntax   vaddint {Oop} vx[0], viz[Z], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands                                                      Offset for the first DW used from the
              3    OUT_OFST        uint8     0..7
                                                              result operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vaddint_v32_v32_p_4p (8, vIn, 0, vecPred);

                   The vaddint_v32_v32_p_4p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
Comments      1.
                   default is "Demapper installed". Therefore, for ensuring correct execution on

the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Intra Vector → Add Intra-Vector → Vector Add Intra-Vector
