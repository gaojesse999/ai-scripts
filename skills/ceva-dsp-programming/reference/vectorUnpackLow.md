# Move And Pack → Unpack → Vector Unpack Low

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Unpack → Vector Unpack Low

Vector Unpack Low

Vector Unpack Low
Performs unpack of either 32-bit or 40-bit source into two low part destinations of either 32-bit
or 40-bit wide determined by the register type.
Available Switches
Qop       Number of atomic operations. 1op ≤ Qop ≤ 4op .
b         The source data is byte to be unpacked into words
u         When used, the destination is zero-extended. The default is sign-extention.
          When used, the part which is not written by the instruction remains unchanged. The
unch
          default is sign-extention.
w         The source data is word (16-bits) to be unpacked into double-words
we        The source data is word with extension (20-bits) to be unpacked into double-words
Intrinsic Names
vunpackl_v32_v32_b
vunpackl_v32_v32_b_u
vunpackl_v32_v32_b_unch
vunpackl_v32_v32_w
vunpackl_v32_v32_w_u
vunpackl_v32_v32_w_unch
vunpackl_v40_v32_b
vunpackl_v40_v32_b_u
vunpackl_v40_v32_b_unch
vunpackl_v40_v32_w
vunpackl_v40_v32_w_u
vunpackl_v40_v32_w_unch
vunpackl_v40_v32_we
vunpackl_v40_v32_we_u
Instruction details in the instruction set specification

Intrinsic     vunpackl_v32_v32_b[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands                                                      Offset for the first DW used from operand
              3    IN1_OFST        uint8     0,4
                                                              2

              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpackl_v32_v32_b_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vunpackl_v32_v32_b_p version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v32_v32_b_u[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands                                                      Offset for the first DW used from operand
              3    IN1_OFST        uint8     0,4
                                                              2

              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpackl_v32_v32_b_u_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vunpackl_v32_v32_b_u_p version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v32_v32_b_unch[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vx[0], vz[0], ?vprX

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
              vRes = vunpackl_v32_v32_b_unch_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpackl_v32_v32_b_unch_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v32_v32_w[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vx[0], vz[0], ?vprX

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
              vRes = vunpackl_v32_v32_w_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vunpackl_v32_v32_w_p version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v32_v32_w_u[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations

Operands
              2    IN1_V32        vec_t                      Input vector operand

              3    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             2
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpackl_v32_v32_w_u_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vunpackl_v32_v32_w_u_p version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v32_v32_w_unch[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vx[0], vz[0], ?vprX

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
              vRes = vunpackl_v32_v32_w_unch_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpackl_v32_v32_w_unch_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v40_v32_b[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
Operands                                                      Offset for the first DW used from operand
              3    IN1_OFST        uint8     0,4
                                                              2

              4    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpackl_v40_v32_b_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vunpackl_v40_v32_b_p version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v40_v32_b_u[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V40         vec40_t                    Output vector operand
Operands                                                      Offset for the first DW used from operand
              3    IN1_OFST        uint8     0,4
                                                              2

              4    IN_VPR          vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpackl_v40_v32_b_u_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vunpackl_v40_v32_b_u_p version.

Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v40_v32_b_unch[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vox[0], vz[0], ?vprX

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
              vRes = vunpackl_v40_v32_b_unch_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpackl_v40_v32_b_unch_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v40_v32_w[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vox[0], vz[0], ?vprX

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
              vRes = vunpackl_v40_v32_w_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vunpackl_v40_v32_w_p version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v40_v32_w_u[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations

Operands
              2    IN1_V40        vec40_t                    Output vector operand

              3    IN1_OFST       uint8     0,4              Offset for the first DW used from operand
                                                             2

4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vunpackl_v40_v32_w_u_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vunpackl_v40_v32_w_u_p version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v40_v32_w_unch[_p]
name
Spec syntax   vunpackl {Qop, b_w [,u_unch]} vox[0], vz[0], ?vprX

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
              vRes = vunpackl_v40_v32_w_unch_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpackl_v40_v32_w_unch_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v40_v32_we[_p]
name
Spec syntax   vunpackl {Qop, we [,u]} vox[0], vz[0], ?vprX

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
              vRes = vunpackl_v40_v32_we_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vunpackl_v40_v32_we_p version.


Main table → Move And Pack → Unpack → Vector Unpack Low
Intrinsic     vunpackl_v40_v32_we_u[_p]
name
Spec syntax   vunpackl {Qop, we [,u]} vox[0], vz[0], ?vprX

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
              vRes = vunpackl_v40_v32_we_u_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vunpackl_v40_v32_we_u_p
Comments      1.
                   version.


Main table → Move And Pack → Unpack → Vector Unpack Low
