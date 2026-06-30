# Logic → Xor → Vector XOR

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Logic → Xor → Vector XOR

Vector XOR

Vector XOR

Performs logic-XOR operation between two 32-bit or 40-bit sources into either 32-bit or 40-bit
destination according to the register type.
Available Switches
        Number of atomic operations. An atomic operation is defined as a single logic-xor
Oop
        operation. 1op ≤ Oop ≤ 8op
Intrinsic Names
vxor_v32_v32_v32
vxor_v40_v40_v32
Instruction details in the instruction set specification
Intrinsic     vxor_v32_v32_v32[_p]
name
Spec syntax   vxor {Oop} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_V32         vec_t                      Input vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vxor_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vxor_v32_v32_v32_p version.


Main table → Logic → Xor → Vector XOR
Intrinsic     vxor_v40_v40_v32[_p]
name
Spec syntax   vxor {Oop} vox[0], voy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
Operands
              3    IN2_V40         vec40_t                    Output vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vxor_v40_v40_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vxor_v40_v40_v32_p version.


Main table → Logic → Xor → Vector XOR
