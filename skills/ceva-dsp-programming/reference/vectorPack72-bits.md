# Move And Pack → Pack → Vector Pack 72-bits

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Pack → Vector Pack 72-bits

Vector Pack 72-bits

Vector Pack 72-bits
Performs packing between 72-bit source parts(32 or 40-bits) into 32-bit or 40-bit destinations
depending on the register type.
Available Switches
         Number of atomic operations. An atomic operation is defined as packing a 72-bit source
Qop
         part into a 32-bit destination.
dweh 40 MSBs of source is used for the pack operation.
dwh      32 MSBs of source is used for the pack operation.
dwl      32 LSBs of source is used for the pack operation.
Intrinsic Names
vpack72_v40_v40_dweh
vpack72_v40_v40_dwl
vpack72_v40_v32_dwh
vpack72_v40_v32_dwl
Instruction details in the instruction set specification
Intrinsic     vpack72_v40_v40_dweh[_p]
name
Spec syntax   vpack72 {Qop ,dweh_dwl} vox[0], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4

result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack72_v40_v40_dweh_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack72_v40_v40_dweh_p version.


Main table → Move And Pack → Pack → Vector Pack 72-bits
Intrinsic     vpack72_v40_v40_dwl[_p]
name
Spec syntax   vpack72 {Qop ,dweh_dwl} vox[0], voz[0], ?vprX

Return type   vec40_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec40_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack72_v40_v40_dwl_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack72_v40_v40_dwl_p version.


Main table → Move And Pack → Pack → Vector Pack 72-bits
Intrinsic     vpack72_v40_v32_dwh[_p]
name
Spec syntax   vpack72 {Qop ,dwh_dwl} vox[0], viz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack72_v40_v32_dwh_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack72_v40_v32_dwh_p version.


Main table → Move And Pack → Pack → Vector Pack 72-bits
Intrinsic     vpack72_v40_v32_dwl[_p]
name
Spec syntax   vpack72 {Qop ,dwh_dwl} vox[0], viz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations

2    IN1_V40        vec40_t                    Output vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack72_v40_v32_dwl_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack72_v40_v32_dwl_p version.


Main table → Move And Pack → Pack → Vector Pack 72-bits
