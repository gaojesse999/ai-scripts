# Arithmetic → Addition → Vector Add 20-bit Word Parts

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Addition → Vector Add 20-bit Word Parts

Vector Add 20-bit Word Parts

Vector Add 20-bit Word Parts
Performs two additions. Each addition is between two sources into destination. The first source is
either 16-bit or 20-bit wide (‘out’ switch) and the second source is 20-bit wide. the destination is
20-bits and packed into 40-bit destination vector register type.
Available Switches
           Number of atomic operations. An atomic operation is defined as a two additions. 1op ≤
Oop
           Oop ≤ 8op
Out        The out switch notify that both sources are treated as 20-bit operands.
Intrinsic Names

vadd20_v40_v32_v40
vadd20_v40_v40_v40_out
Instruction details in the instruction set specification
Intrinsic     vadd20_v40_v32_v40[_p]
name
Spec syntax   vadd20 {Oop} vox[0], vy[0], voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands
              3    IN2_V32        vec_t                      Input vector operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vadd20_v40_v32_v40_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vadd20_v40_v32_v40_p version.


Main table → Arithmetic → Addition → Vector Add 20-bit Word Parts
Intrinsic     vadd20_v40_v40_v40_out[_p]
name
Spec syntax   vadd20 {Oop, out} vox[0], voy[0], voz[0], ?vprX

Return type   vec40_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands
              3    IN2_V40        vec40_t                    Output vector operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vadd20_v40_v40_v40_out_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vadd20_v40_v40_v40_out_p
Comments      1.
                   version.


Main table → Arithmetic → Addition → Vector Add 20-bit Word Parts
