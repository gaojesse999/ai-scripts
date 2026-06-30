# Move And Pack → Unpack → Vector Unpack 32-bits

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Unpack → Vector Unpack 32-bits

Vector Unpack 32-bits

Vector Unpack 32-bits
Performs unpack of 32-bit source into high or low parts of destinations of either 64-bit or 72-bit
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
vunpack32_v32_v32_dwh
vunpack32_v32_v32_dwh_unch
vunpack32_v32_v32_dwl

vunpack32_v32_v32_dwl_u
vunpack32_v32_v40_dwh
vunpack32_v32_v40_dwh_u
vunpack32_v32_v40_dwh_u_unch
vunpack32_v32_v40_dwh_unch
Instruction details in the instruction set specification
Intrinsic     vunpack32_v32_v32_dwh[_p]
name
Spec syntax   vunpack32 {Qop ,dwh [,unch]} vx[0], viz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands                                                    Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                            2

              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack32_v32_v32_dwh_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpack32_v32_v32_dwh_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector Unpack 32-bits
Intrinsic     vunpack32_v32_v32_dwh_unch[_p]
name
Spec syntax   vunpack32 {Qop ,dwh [,unch]} vx[0], viz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands                                                    Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                            2

              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack32_v32_v32_dwh_unch_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpack32_v32_v32_dwh_unch_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector Unpack 32-bits
Intrinsic     vunpack32_v32_v32_dwl[_p]
name
Spec syntax   vunpack32 {Qop ,dwl [,u]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand

Operands                                                     Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                             2

              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack32_v32_v32_dwl_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpack32_v32_v32_dwl_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector Unpack 32-bits
Intrinsic     vunpack32_v32_v32_dwl_u[_p]
name
Spec syntax   vunpack32 {Qop ,dwl [,u]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                             2

              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack32_v32_v32_dwl_u_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpack32_v32_v32_dwl_u_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector Unpack 32-bits
Intrinsic     vunpack32_v32_v40_dwh[_p]
name
Spec syntax   vunpack32 {Qop, dwh [,u][,unch]} vx[0], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands                                                    Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                            2

              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack32_v32_v40_dwh_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpack32_v32_v40_dwh_p
Comments      1.

version.


Main table → Move And Pack → Unpack → Vector Unpack 32-bits
Intrinsic     vunpack32_v32_v40_dwh_u[_p]
name
Spec syntax   vunpack32 {Qop, dwh [,u][,unch]} vx[0], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands                                                    Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                            2

              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack32_v32_v40_dwh_u_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpack32_v32_v40_dwh_u_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector Unpack 32-bits
Intrinsic     vunpack32_v32_v40_dwh_u_unch[_p]
name
Spec syntax   vunpack32 {Qop, dwh [,u][,unch]} vx[0], voz[0], ?vprX
Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands                                                    Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                            2

              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack32_v32_v40_dwh_u_unch_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vunpack32_v32_v40_dwh_u_unch_p version.


Main table → Move And Pack → Unpack → Vector Unpack 32-bits
Intrinsic     vunpack32_v32_v40_dwh_unch[_p]
name
Spec syntax   vunpack32 {Qop, dwh [,u][,unch]} vx[0], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands                                                    Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4

2

              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpack32_v32_v40_dwh_unch_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpack32_v32_v40_dwh_unch_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector Unpack 32-bits
