# Logic → Xor → Vector Semi-Complex XOR

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Logic → Xor → Vector Semi-Complex XOR

Vector Semi-Complex XOR

Vector Semi-Complex XOR
Performs semi-complex logic-XOR operation between 2-bit complex sources (16 sources per 32-
bit vx[X]) and 1-bit real sources (16 sources per vy[Y]p). The Logix-XOR operation is
performed on a bit-by-bit basis and the results are written into either 32-bit or 40-bit complex
destination according to the register type.
Available Switches
           Number of atomic operations. An atomic operation is defined as a single semi-complex
Oop
           logic-xor operation.
Intrinsic Names
vxorxr_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vxorxr_v32_v32_v32[_p]
name
Spec syntax   vxorxr {Oop} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand

Operands
              3    IN2_V32         vec_t                      Input vector operand

              4    IN2_OFST        uint8     0,4
                                                              Offset for the first DW used from operand
                                                              3

              5    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vxorxr_v32_v32_v32_p (8, vIn, vIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vxorxr_v32_v32_v32_p version.


Main table → Logic → Xor → Vector Semi-Complex XOR
