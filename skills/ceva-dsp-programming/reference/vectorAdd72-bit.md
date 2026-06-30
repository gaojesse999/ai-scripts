# Arithmetic → Addition → Vector Add 72-bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Addition → Vector Add 72-bit

Vector Add 72-bit

Vector Add 72-bit
Performs addition between two sources into destinations. The first source is 64-bit or 72-bits
wide (‘out’ switch) and the second source is 72-bit wide.The destination is 72-bit vector register
type.
Available Switches
Out         The out switch notify that both sources are treated as 72-bit operands.
Qop         Number of atomic operations. An atomic operation is defined as a single addition.
Intrinsic Names
vadd72_v40_v32_v40
vadd72_v40_v40_v40_out
Instruction details in the instruction set specification
Intrinsic     vadd72_v40_v32_v40[_p]
name
Spec syntax   vadd72 {Qop} vox[0], vy[0], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands
              3    IN2_V32        vec_t                      Input vector operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vadd72_v40_v32_v40_p (4, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vadd72_v40_v32_v40_p version.


Main table → Arithmetic → Addition → Vector Add 72-bit
Intrinsic     vadd72_v40_v40_v40_out[_p]
name
Spec syntax   vadd72 {Qop, out} vox[0], voy[0], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands

3    IN2_V40        vec40_t                    Output vector operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vadd72_v40_v40_v40_out_p (4, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vadd72_v40_v40_v40_out_p
Comments      1.
                   version.


Main table → Arithmetic → Addition → Vector Add 72-bit
