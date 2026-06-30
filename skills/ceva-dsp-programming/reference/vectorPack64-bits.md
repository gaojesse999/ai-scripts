# Move And Pack → Pack → Vector Pack 64-bits

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Pack → Vector Pack 64-bits

Vector Pack 64-bits

Vector Pack 64-bits
Performs packing between 64-bit source parts(32-bits) into a 32-bit or 40-bit destination
depending on the register type.
Available Switches
       Number of atomic operations. An atomic operation is defined as packing a 64-bit source
Qop
       part into a 32-bit or 40-bit destination. 1op ≤ Qop ≤ 4op
dwh 32 MSBs of source is used.
dwl 32 LSBs of source is used.
Intrinsic Names
vpack64_v32_v32_dwh
vpack64_v32_v32_dwl
Instruction details in the instruction set specification
Intrinsic     vpack64_v32_v32_dwh[_p]
name
Spec syntax   vpack64 {Qop ,dwh_dwl} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand

4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack64_v32_v32_dwh_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack64_v32_v32_dwh_p version.


Main table → Move And Pack → Pack → Vector Pack 64-bits
Intrinsic     vpack64_v32_v32_dwl[_p]
name
Spec syntax   vpack64 {Qop ,dwh_dwl} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vpack64_v32_v32_dwl_p (4, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vpack64_v32_v32_dwl_p version.


Main table → Move And Pack → Pack → Vector Pack 64-bits
