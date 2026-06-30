# Floating Point → Float Special Operations → Vector Short Integer to

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Special Operations → Vector Short Integer to
Floating Point

Vector Short Integer to Floating Point

Vector Short Integer to Floating Point
Performs a conversion of a signed/unsigned short integer into a 32-bit single precision floating-
point source destination. The sources and the destination are either 32-bit or 40-bit wide
determined by the vector register type.
Available Switches
None
Intrinsic Names
vsint2flp_v32_v32
vsint2flp_v32_v32_uns
Instruction details in the instruction set specification
Intrinsic     vsint2flp_v32_v32[_p]
name
Spec syntax   vsint2flp {Oop [,uns]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP              uint8     1..8               Number of atomic operations
              2    IN1_V32          vec_t                        Input vector operand
Operands                                                         Offset for the first DW used from operand
              3    IN1_OFST         uint8     0,4
                                                                 2

              4    IN_VPR           vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsint2flp_v32_v32_p (8, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsint2flp_v32_v32_p version.


Main table → Floating Point → Float Special Operations → Vector Short Integer to
Floating Point
Intrinsic     vsint2flp_v32_v32_uns[_p]
name
Spec syntax   vsint2flp {Oop [,uns]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP              uint8     1..8               Number of atomic operations
              2    IN1_V32          vec_t                        Input vector operand
Operands                                                         Offset for the first DW used from operand
              3    IN1_OFST         uint8     0,4
                                                                 2

              4    IN_VPR           vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vsint2flp_v32_v32_uns_p (8, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vsint2flp_v32_v32_uns_p version.

Main table → Floating Point → Float Special Operations → Vector Short Integer to
Floating Point
