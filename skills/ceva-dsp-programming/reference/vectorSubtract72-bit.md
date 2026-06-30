# Arithmetic → Subtract → Vector Subtract 72-bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Subtract → Vector Subtract 72-bit

Vector Subtract 72-bit

Vector Subtract 72-bit
Performs subtraction between two sources into destinations. The first source is 64-bit or 72-bits
wide (‘out’ switch) and the second source is 72-bit wide. The destination is 72-bit vector register
type.
Available Switches

Qop       Number of atomic operations. An atomic operation is defined as a single addition.
          The inv switch notify that the second operand is replaced with the first operand, resulting
inv
          voy[0] - vx[0] operation.
out       The out switch notify that both sources are treated as 72-bit operands.
Intrinsic Names
vsub72_v40_v40_v40_out
vsub72_v32_v40_v40_inv
vsub72_v32_v40_v40
Instruction details in the instruction set specification
Intrinsic     vsub72_v40_v40_v40_out[_p]
name
Spec syntax   vsub72 {Qop, out} vox[0], voy[0], voz[0], ?vprX

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
              vRes = vsub72_v40_v40_v40_out_p (4, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vsub72_v40_v40_v40_out_p
Comments      1.
                   version.


Main table → Arithmetic → Subtract → Vector Subtract 72-bit
Intrinsic     vsub72_v32_v40_v40_inv[_p]
name
Spec syntax   vsub72 {Qop, inv} vx[0], voy[0], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8      1..4            Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands
              3    IN2_V40        vec40_t                    Output vector operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsub72_v32_v40_v40_inv_p (4, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vsub72_v32_v40_v40_inv_p
Comments      1.
                   version.


Main table → Arithmetic → Subtract → Vector Subtract 72-bit
Intrinsic     vsub72_v32_v40_v40[_p]
name
Spec syntax   vsub72 {Qop} vx[0], voy[0], voz[0], ?vprX

Return type   vec40_t

              1    QOP             uint8     1..4             Number of atomic operations

2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_V40         vec40_t                    Output vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec40_t vIn2;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsub72_v32_v40_v40_p (4, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsub72_v32_v40_v40_p version.


Main table → Arithmetic → Subtract → Vector Subtract 72-bit
