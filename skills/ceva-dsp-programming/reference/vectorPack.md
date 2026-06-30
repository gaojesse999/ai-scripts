# Move And Pack → Pack → Vector Pack

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Pack → Vector Pack

Vector Pack

Vector Pack
Performs packing between two 32-bit sources parts into 32-bit destination.
Available Switches
     Number of atomic operations. An atomic operation is defined as packing two words or
     four bytes into one destination. Used for two vector sources, while the first vector source
Ohop
     is always fully read, the second vector source number of atomic operation is set by Ohop.
     5op œ Ohop œ 8op
bh       b1 and b3 are packed into the destination
bl       b0 and b2 are packed into the destination
we       The source data is high part word with 4-bit extension (20-bits) to be packed.
wh       High words are packed into the destination
wl       Low words are packed into the destination
Intrinsic Names
vpack_v40_v40_v32_bh_Ohop

vpack_v40_v40_v32_bl_Ohop
vpack_v40_v40_v32_wh_Ohop
vpack_v40_v40_v32_wl_Ohop
vpack_v32_v32_bh
vpack_v32_v32_bl
vpack_v32_v32_wh
vpack_v32_v32_wl
vpack_v40_v32_bh
vpack_v40_v32_bl
vpack_v40_v32_wh
vpack_v40_v32_wl
vpack_v40_v32_we
Instruction details in the instruction set specification
Intrinsic     vpack_v40_v40_v32_bh_Ohop[_p]
name
Spec syntax   vpack {Ohop, wl_wh_bl_bh} vox[0],voy[0], vz[0], ?vprX

Return type   vec_t

              1    OHOP           uint8     5..8            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
Operands
              3    IN2_V40        vec40_t                   Output vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v40_v40_v32_bh_Ohop_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vpack_v40_v40_v32_bh_Ohop_p
Comments      1.
                   version.


Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v40_v40_v32_bl_Ohop[_p]
name
Spec syntax   vpack {Ohop, wl_wh_bl_bh} vox[0],voy[0], vz[0], ?vprX

Return type   vec_t

              1    OHOP           uint8     5..8            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
Operands
              3    IN2_V40        vec40_t                   Output vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v40_v40_v32_bl_Ohop_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vpack_v40_v40_v32_bl_Ohop_p
Comments      1.
                   version.


Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v40_v40_v32_wh_Ohop[_p]
name
Spec syntax   vpack {Ohop, wl_wh_bl_bh} vox[0],voy[0], vz[0], ?vprX
Return type   vec_t

              1    OHOP           uint8     5..8            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
Operands
              3    IN2_V40        vec40_t                   Output vector operand

4    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v40_v40_v32_wh_Ohop_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vpack_v40_v40_v32_wh_Ohop_p
              1.
                   version.
                   When vpack{wh} result is allocated with a voZ register, the guard bits are
                   cleared. Therefore, if the result is read in a subsequent calculation as 40-bits,
                   it is treated as unsigned. However, in case viZ is allocated for the result, the
Comments           result might be treated as signed (sign extended) in the subsequent
              2.   calculation. To avoid inconsistent results that depend on allocated result
                   register when the result is used later in a 40-bit calculation, use a vec40_t
                   variable for assuring a voZ register is allocated, or - use vpack{we} for
                   copying the guard bits, or - bind the vec_t result variable to a viZ/voZ register
                   depending on the desired result (less prefered).


Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v40_v40_v32_wl_Ohop[_p]
name
Spec syntax   vpack {Ohop, wl_wh_bl_bh} vox[0],voy[0], vz[0], ?vprX

Return type   vec_t

              1    OHOP           uint8     5..8            Number of atomic operations
              2    IN1_V40        vec40_t                   Output vector operand
Operands
              3    IN2_V40        vec40_t                   Output vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vIn;
              vec40_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v40_v40_v32_wl_Ohop_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vpack_v40_v40_v32_wl_Ohop_p
Comments      1.
                   version.

Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v32_v32_bh[_p]
name
Spec syntax   vpack {Qop, wl_wh_bl_bh} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand

Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0,4
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v32_v32_bh_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack_v32_v32_bh_p version.


Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v32_v32_bl[_p]
name
Spec syntax   vpack {Qop, wl_wh_bl_bh} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0,4
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v32_v32_bl_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack_v32_v32_bl_p version.


Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v32_v32_wh[_p]
name
Spec syntax   vpack {Qop, wl_wh_bl_bh} vx[0], vz[0], ?vprX

Return type   vec_t
              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0,4
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v32_v32_wh_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack_v32_v32_wh_p version.


Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v32_v32_wl[_p]
name

Spec syntax   vpack {Qop, wl_wh_bl_bh} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V32         vec_t                        Input vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0,4
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v32_v32_wl_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack_v32_v32_wl_p version.


Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v40_v32_bh[_p]
name
Spec syntax   vpack {Qop, wl_wh_bl_bh} vox[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V40         vec40_t                      Output vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0,2,4,6
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v40_v32_bh_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack_v40_v32_bh_p version.


Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v40_v32_bl[_p]
name
Spec syntax   vpack {Qop, wl_wh_bl_bh} vox[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V40         vec40_t                      Output vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0,2,4,6
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec40_t vIn;
              vec_t vRes;

C example     vprex_t vecPred;
              ...
              vRes = vpack_v40_v32_bl_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack_v40_v32_bl_p version.


Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v40_v32_wh[_p]
name
Spec syntax   vpack {Qop, wl_wh_bl_bh} vox[0], vz[0], ?vprX

Return type   vec_t
              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V40         vec40_t                      Output vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0,2,4,6
                                                                result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v40_v32_wh_p (4, vIn, 0, vecPred);

              1.   IN_VPR last operand is relevant only for vpack_v40_v32_wh_p version.
                   When vpack{wh} result is allocated with a voZ register, the guard bits are
                   cleared. Therefore, if the result is read in a subsequent calculation as 40-bits,
                   it is treated as unsigned. However, in case viZ is allocated for the result, the
Comments           result might be treated as signed (sign extended) in the subsequent
              2.   calculation. To avoid inconsistent results that depend on allocated result
                   register when the result is used later in a 40-bit calculation, use a vec40_t
                   variable for assuring a voZ register is allocated, or - use vpack{we} for
                   copying the guard bits, or - bind the vec_t result variable to a viZ/voZ register
                   depending on the desired result (less prefered).


Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v40_v32_wl[_p]
name
Spec syntax   vpack {Qop, wl_wh_bl_bh} vox[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4               Number of atomic operations
              2    IN1_V40         vec40_t                      Output vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST        uint8     0,2,4,6

result operand
              4    IN_VPR          vprex_t                      Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v40_v32_wl_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack_v40_v32_wl_p version.


Main table → Move And Pack → Pack → Vector Pack
Intrinsic     vpack_v40_v32_we[_p]
name
Spec syntax   vpack {Qop, we} vox[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8      1..4               Number of atomic operations
              2    IN1_V40        vec40_t                       Output vector operand
Operands                                                        Offset for the first DW used from the
              3    OUT_OFST       uint8      0,2,4,6
                                                                result operand
              4    IN_VPR         vprex_t                       Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack_v40_v32_we_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack_v40_v32_we_p version.


Main table → Move And Pack → Pack → Vector Pack
