# Floating Point → Float Special Operations → Vector Floating Point to Short

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Special Operations → Vector Floating Point to Short
Integer

Vector Floating Point to Short Integer

Vector Floating Point to Short Integer
Performs a conversion of the absolute value of a 32-bit single precision floating point number
into signed/unsigned short-integer representation. In case the destination’s type is signed short-
integer, the MSB bit is the same as the input’s sign-bit. This instruction is part of the non-native
VFLPSINT operation.
Available Switches
None
Intrinsic Names
vflp2sint_v32_v32
vflp2sint_v32_v32_u
Instruction details in the instruction set specification
Intrinsic     vflp2sint_v32_v32[_p]
name
Spec syntax   vflp2sint {Qop [,u]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP              uint8     1..4               Number of atomic operations
              2    IN1_V32          vec_t                        Input vector operand
Operands                                                         Offset for the first DW used from the
              3    OUT_OFST         uint8     0,4
                                                                 result operand
              4    IN_VPR           vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflp2sint_v32_v32_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vflp2sint_v32_v32_p version.


Main table → Floating Point → Float Special Operations → Vector Floating Point to Short
Integer
Intrinsic     vflp2sint_v32_v32_u[_p]
name
Spec syntax   vflp2sint {Qop [,u]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP              uint8     1..4               Number of atomic operations
              2    IN1_V32          vec_t                        Input vector operand
Operands                                                         Offset for the first DW used from the
              3    OUT_OFST         uint8     0,4

result operand
              4    IN_VPR           vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vflp2sint_v32_v32_u_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vflp2sint_v32_v32_u_p version.


Main table → Floating Point → Float Special Operations → Vector Floating Point to Short
Integer
