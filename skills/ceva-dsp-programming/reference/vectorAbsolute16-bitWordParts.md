# Arithmetic → Absolute → Vector Absolute 16-bit Word Parts

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Absolute → Vector Absolute 16-bit Word Parts

Vector Absolute 16-bit Word Parts

Vector Absolute 16-bit Word Parts
Performs two absolute operations. For each single absolute operation, the source is 16-bit, the
destination are either 16-bit or 20-bit determined by the vector register type. The two operation
results are packed into either 32-bit or 40-bit destination, respectively.
Available Switches
                  Number of atomic operations. An atomic operation is defined as two absolute
Oop
                  operations. 1op ≤ Oop ≤ 8op

signmsb           When used, the result MSB bit gets the same value as the sign bit of the source,
uns               When used, the evaluated source operand is unsigned. The default is signed.
Intrinsic Names
vabs16_v32_v32
vabs16_v32_v32_signmsb
vabs16_v32_v32_signmsb_uns
vabs16_v32_v32_uns
Instruction details in the instruction set specification
Intrinsic     vabs16_v32_v32[_p]
name
Spec syntax   vabs16 {Oop} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8          Number of atomic operations
Operands      2    IN1_V32         vec_t                   Input vector operand
              3    IN_VPR          vprex_t                 Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vabs16_v32_v32_p (8, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vabs16_v32_v32_p version.


Main table → Arithmetic → Absolute → Vector Absolute 16-bit Word Parts
Intrinsic     vabs16_v32_v32_signmsb[_p]
name
Spec syntax   vabs16 {Oop [,signmsb][,uns]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vabs16_v32_v32_signmsb_p (8, vIn, vecPred);

                   IN_VPR last operand is relevant only for vabs16_v32_v32_signmsb_p
Comments      1.
                   version.


Main table → Arithmetic → Absolute → Vector Absolute 16-bit Word Parts
Intrinsic     vabs16_v32_v32_signmsb_uns[_p]
name
Spec syntax   vabs16 {Oop [,signmsb][,uns]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vabs16_v32_v32_signmsb_uns_p (8, vIn, vecPred);

                   IN_VPR last operand is relevant only for vabs16_v32_v32_signmsb_uns_p
Comments      1.
                   version.

Main table → Arithmetic → Absolute → Vector Absolute 16-bit Word Parts
Intrinsic     vabs16_v32_v32_uns[_p]
name
Spec syntax   vabs16 {Oop [,signmsb][,uns]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands
              2    IN1_V32        vec_t                     Input vector operand
            3    IN_VPR         vprex_t                      Vector predicate operand
            vec_t vIn;
            vec_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vabs16_v32_v32_uns_p (8, vIn, vecPred);

Comments    1.   IN_VPR last operand is relevant only for vabs16_v32_v32_uns_p version.


Main table → Arithmetic → Absolute → Vector Absolute 16-bit Word Parts
