# Intra Vector → Add Intra-Vector → Vector Add Intra-Vector Word Parts

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Intra Vector → Add Intra-Vector → Vector Add Intra-Vector Word Parts

Vector Add Intra-Vector Word Parts

Vector Add Intra-Vector Word Parts
Performs intra-vector addition between complex sources in the same vector. Each complex
number consists of real 16-bit part and imaginary 16-bit part. The intravector addition results for
each complex part packed into 32-bit or 40-bit register destination determined by the vector
register type.
Available Switches
           Number of atomic operations. An atomic operation is defined as adding a single register
Oop
           in split words. 1op ≤ Oop ≤ 8op
s          Saturation switch.
Intrinsic Names
vaddintwx_v32_v40_p_4p
vaddintwx_v32_v40_s_p_4p
vaddintwx_v32_v32_p_4p
vaddintwx_v32_v32_s_p_4p
Instruction details in the instruction set specification
Intrinsic     vaddintwx_v32_v40_p_4p
name
Spec syntax   vaddintwx {Oop [,s_sw]} vx[0], voz[Z], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vaddintwx_v32_v40_p_4p (8, vIn, 0, vecPred);

                   The vaddintwx_v32_v40_p_4p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
Comments      1.
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                   the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Intra Vector → Add Intra-Vector → Vector Add Intra-Vector Word Parts
Intrinsic     vaddintwx_v32_v40_s_p_4p
name
Spec syntax   vaddintwx {Oop [,s_sw]} vx[0], voz[Z], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vaddintwx_v32_v40_s_p_4p (8, vIn, 0, vecPred);

                   The vaddintwx_v32_v40_s_p_4p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
Comments      1.
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                the HW, the -mno-demapper Compiler switch must be specified in case
                Demapper is not installed.


Main table → Intra Vector → Add Intra-Vector → Vector Add Intra-Vector Word Parts
Intrinsic     vaddintwx_v32_v32_p_4p
name
Spec syntax   vaddintwx {Oop} vx[0], viz[Z], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vaddintwx_v32_v32_p_4p (8, vIn, 0, vecPred);

                   The vaddintwx_v32_v32_p_4p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
Comments      1.
                   default is "Demapper installed". Therefore, for ensuring correct execution on

the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Intra Vector → Add Intra-Vector → Vector Add Intra-Vector Word Parts
Intrinsic     vaddintwx_v32_v32_s_p_4p
name
Spec syntax   vaddintwx {Oop, s} vx[0], viz[Z], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0..7
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vaddintwx_v32_v32_s_p_4p (8, vIn, 0, vecPred);

                   The vaddintwx_v32_v32_s_p_4p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
Comments      1.
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                   the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Intra Vector → Add Intra-Vector → Vector Add Intra-Vector Word Parts
