# Bit Manipulation → Bit Pack → Vector Bit Pack

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Bit Pack → Vector Bit Pack

Vector Bit Pack

Vector Bit Pack
Performs packing of specific bits from source into 32-bit destination.
Available Switches
Oop        Number of atomic operations.
b          The bits are extracted from bytes
dw         The bits are extracted from double-words
w          The bits are extracted from words
Intrinsic Names
vbpack_v32_uimm5_v40_p_7p
vbpack_v32_v32_b_p_4p
vbpack_v32_v32_dw_p_4p
vbpack_v32_v32_w_p_4p
vbpack_v32_c32_v40_p_8p
Instruction details in the instruction set specification
Intrinsic     vbpack_v32_uimm5_v40_p_7p
name
Spec syntax   vbpack vi00, vi1, vi2, vi3 #uimm5, voz[Z], ?vprX

Return type   vec40_t


              1
                                                             Input vector operand (register vi0 is
                   IN1_VI0         vec_t
                                                             expected)
                                                             Input vector operand (register vi1 is

2    IN2_VI1         vec_t
                                                             expected)
                                                             Input vector operand (register vi2 is
              3    IN3_VI2         vec_t
                                                             expected)
Operands
                                                             Input vector operand (register vi3 is
              4    IN4_VI3         vec_t
                                                             expected)
              5    IN5_UIMM5       uint16    0..31           5 bit unsigned immediate
                                                             Offset for the first DW used from the
              6    OUT_OFST        uint8     0..7
                                                             result operand
              7    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec40_t vRes;
              vprex_t vecPred;
              ...
              vRes = vbpack_v32_uimm5_v40_p_7p (vIn, vIn2, vIn3, vIn4, 2, 0, vecPred);

Comments


Main table → Bit Manipulation → Bit Pack → Vector Bit Pack
Intrinsic     vbpack_v32_v32_b_p_4p
name
Spec syntax   vbpack {Oop, b_w_dw} vx[0], vz[Z], ?vprX

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
              vRes = vbpack_v32_v32_b_p_4p (8, vIn, 0, vecPred);

Comments


Main table → Bit Manipulation → Bit Pack → Vector Bit Pack
Intrinsic     vbpack_v32_v32_dw_p_4p
name
Spec syntax   vbpack {Oop, b_w_dw} vx[0], vz[Z], ?vprX

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
              vRes = vbpack_v32_v32_dw_p_4p (8, vIn, 0, vecPred);

Comments


Main table → Bit Manipulation → Bit Pack → Vector Bit Pack
Intrinsic     vbpack_v32_v32_w_p_4p
name
Spec syntax   vbpack {Oop, b_w_dw} vx[0], vz[Z], ?vprX

Return type   vec_t
            1    OOP            uint8     1..8             Number of atomic operations
            2    IN1_V32        vec_t                      Input vector operand
Operands                                                   Offset for the first DW used from the
            3    OUT_OFST       uint8     0..7
                                                           result operand
            4    IN_VPR         vprex_t                    Vector predicate operand
            vec_t vIn;
            vec_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vbpack_v32_v32_w_p_4p (8, vIn, 0, vecPred);

Comments


Main table → Bit Manipulation → Bit Pack → Vector Bit Pack
Intrinsic     vbpack_v32_c32_v40_p_8p
name
Spec syntax   vbpack vi00, vi1, vi2, vi3 vcYp, voz[Z], ?vprX

Return type   vec40_t


              1
                                                              Input vector operand (register vi0 is
                   IN1_VI0         vec_t
                                                              expected)
                                                              Input vector operand (register vi1 is
              2    IN2_VI1         vec_t
                                                              expected)
                                                              Input vector operand (register vi2 is
              3    IN3_VI2         vec_t
                                                              expected)

Operands                                                      Input vector operand (register vi3 is
              4    IN4_VI3         vec_t
                                                              expected)
              5    IN5_C32         coef_t                     Coefficient operand
              6    IN5_PART        uint8     LOW,HIGH         Word part which is used for operand 5

Offset for the first DW used from the
              7    OUT_OFST        uint8     0..7
                                                              result operand
              8    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vIn3;
              vec_t vIn4;
C example     vec40_t vRes;
              coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vbpack_v32_c32_v40_p_8p (vIn, vIn2, vIn3, vIn4, vcoefIn, LOW, 0, vecPred);

Comments


Main table → Bit Manipulation → Bit Pack → Vector Bit Pack
