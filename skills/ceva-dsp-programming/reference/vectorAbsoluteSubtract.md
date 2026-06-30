# Arithmetic → Absolute Subtract → Vector Absolute Subtract

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Absolute Subtract → Vector Absolute Subtract

Vector Absolute Subtract

Vector Absolute Subtract
Performs subtraction and absolute value between two sources. The sources are either 8-bit or 16-
bit wide. The results are 16-bit and packed into 32-bit or 40-bit destination determined by the
vector register type.
Available Switches
         Number of atomic operations. An atomic operation is defined as a two parallel word
Oop
         absolute-subtraction operation each is in word resolution.
         Number of atomic operations. An atomic operation is defined as a four parallel byte
Qop
         absolute-subtraction operation each is in byte resolution.
b        The absolute-subtraction operation is performed on bytes
w        The absolute-subtraction operation is performed on words
Intrinsic Names
vabssub_v32_v32_v32_b
vabssub_v32_v32_v32_w
Instruction details in the instruction set specification
Intrinsic     vabssub_v32_v32_v32_b[_p]
name
Spec syntax   vabssub {Qop ,b} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2
Operands
              4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vabssub_v32_v32_v32_b_p (4, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vabssub_v32_v32_v32_b_p
Comments      1.
                   version.


Main table → Arithmetic → Absolute Subtract → Vector Absolute Subtract
Intrinsic     vabssub_v32_v32_v32_w[_p]
name
Spec syntax   vabssub {Oop ,w} vx[X], vy[Y], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations

2    IN1_V32         vec_t                      Input vector operand

              3    IN1_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              2
Operands
              4    IN2_V32         vec_t                      Input vector operand

              5    IN2_OFST        uint8     0..7
                                                              Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vabssub_v32_v32_v32_w_p (8, vIn, 0, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vabssub_v32_v32_v32_w_p
Comments      1.
                   version.


Main table → Arithmetic → Absolute Subtract → Vector Absolute Subtract
