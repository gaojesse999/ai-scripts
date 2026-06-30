# Arithmetic → Addition → Vector Add 40-bit

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Addition → Vector Add 40-bit

Vector Add 40-bit

Vector Add 40-bit
Performs addition between two sources into destination. The first source is 32-bit or 40-bit wide
(‘out’ switch) and the second source is 40-bit wide. The destinations are 40-bit wide.
Available Switches

Oop        Number of atomic operations. An atomic operation is defined as a single addition.
Out        The out switch notify that both sources are treated as 40-bit operands.
Intrinsic Names
vadd40_v40_v32_v40
vadd40_v40_v40_v40_out
Instruction details in the instruction set specification
Intrinsic     vadd40_v40_v32_v40[_p]
name
Spec syntax   vadd40 {Oop} vox[0], vy[0], voz[0], ?vprX

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
              vRes = vadd40_v40_v32_v40_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vadd40_v40_v32_v40_p version.


Main table → Arithmetic → Addition → Vector Add 40-bit
Intrinsic     vadd40_v40_v40_v40_out[_p]
name
Spec syntax   vadd40 {Oop, out} vox[0], voy[0], voz[0], ?vprX

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
              vRes = vadd40_v40_v40_v40_out_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vadd40_v40_v40_v40_out_p
Comments      1.
                   version.


Main table → Arithmetic → Addition → Vector Add 40-bit
