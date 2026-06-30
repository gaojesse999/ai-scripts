# Move And Pack → Unpack → Vector unpack 40-bits

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Unpack → Vector unpack 40-bits

Vector unpack 40-bits

Vector unpack 40-bits
Performs unpack of 40-bit source into high or low parts of destinations of either 64-bit or 72-bit
wide determined by the register type.
Available Switches
Qop       Number of atomic operations. 1op ≤ Qop ≤ 4op.
dwh       When used the result is written to the high part of the destination.
dwl       When used the result is written to the low part of the destination.
u         When used, the destination is zero-extended. The default is sign-extended.
          When used, the part which is not written by the instruction remains unchanged. The
unch
          default is cleared.
Intrinsic Names
vunpack40_v40_v32_dwh
vunpack40_v40_v32_dwh_unch
vunpack40_v40_v32_dwl
vunpack40_v40_v32_dwl_u
Instruction details in the instruction set specification
Intrinsic     vunpack40_v40_v32_dwh[_p]
name
Spec syntax   vunpack40 {Qop, dwh [,unch]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
Operands                                                    Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                            2

              4    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack40_v40_v32_dwh_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpack40_v40_v32_dwh_p
Comments      1.
                   version.

Main table → Move And Pack → Unpack → Vector unpack 40-bits
Intrinsic     vunpack40_v40_v32_dwh_unch[_p]
name
Spec syntax   vunpack40 {Qop, dwh [,unch]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
Operands                                                    Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                            2

              4    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack40_v40_v32_dwh_unch_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpack40_v40_v32_dwh_unch_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector unpack 40-bits
Intrinsic     vunpack40_v40_v32_dwl[_p]
name
Spec syntax   vunpack40 {Qop, dwl [,u]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                             2

              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack40_v40_v32_dwl_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpack40_v40_v32_dwl_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector unpack 40-bits
Intrinsic     vunpack40_v40_v32_dwl_u[_p]
name
Spec syntax   vunpack40 {Qop, dwl [,u]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4

2

              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack40_v40_v32_dwl_u_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpack40_v40_v32_dwl_u_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector unpack 40-bits
