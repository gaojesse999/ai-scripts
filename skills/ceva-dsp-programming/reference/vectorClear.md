# Move And Pack → Clear → Vector Clear

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Clear → Vector Clear

Vector Clear

Vector Clear
Performs clearance of destination. The destination is either 32-bit or 40-bit wide according to the
register type.
Available Switches
       Number of atomic operations. An atomic operation is defined as a single clear operation.
Oop
       1op ≤ Oop ≤ 8op
       Number of atomic operations. An atomic operation is defined as a single clear operation.
Qop
       1op ≤ Qop ≤ 4op
Intrinsic Names
vclr_c32_1op
vclr_c32_2op
vclr_c32_3op
vclr_c32_4op
vclr_v32
Instruction details in the instruction set specification
Intrinsic     vclr_c32_1op[_p]
name
Spec syntax   vclr {Qop} vc0, ?vprX

Return type   coef_t

Operands      1    IN_VPR         vprex_t                    Vector predicate operand
              coef_t vcoefRes;
              vprex_t vecPred;
C example     ...
              vcoefRes = vclr_c32_1op_p (vecPred);

Comments      1.   IN_VPR last operand is relevant only for vclr_c32_1op_p version.


Main table → Move And Pack → Clear → Vector Clear
Intrinsic     vclr_c32_2op[_p]
name
Spec syntax   vclr {Qop} vc0, ?vprX

Return type   coef_t

                                                             Coefficient result operand (register vc1 is
              1    RES2_VC1       coef_t
Operands                                                     expected)
              2    IN_VPR         vprex_t                    Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     vprex_t vecPred;
              ...
              vcoefRes1 = vclr_c32_2op_p (vcoefRes2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vclr_c32_2op_p version.


Main table → Move And Pack → Clear → Vector Clear
Intrinsic     vclr_c32_3op[_p]
name
Spec syntax   vclr {Qop} vc0, ?vprX

Return type   coef_t

                                                             Coefficient result operand (register vc1 is
              1    RES2_VC1       coef_t
                                                             expected)

Operands                                                     Coefficient result operand (register vc2 is
              2    RES3_VC2       coef_t
                                                             expected)
              3    IN_VPR         vprex_t                    Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vclr_c32_3op_p (vcoefRes2, vcoefRes3, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vclr_c32_3op_p version.


Main table → Move And Pack → Clear → Vector Clear
Intrinsic     vclr_c32_4op[_p]
name
Spec syntax   vclr {Qop} vc0, ?vprX

Return type   coef_t

                                                              Coefficient result operand (register vc1 is
              1    RES2_VC1        coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              2    RES3_VC2        coef_t
Operands                                                      expected)
                                                              Coefficient result operand (register vc3 is
              3    RES4_VC3        coef_t
                                                              expected)
              4    IN_VPR          vprex_t                    Vector predicate operand
              coef_t vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
C example     coef_t vcoefRes4;
              vprex_t vecPred;
              ...
              vcoefRes1 = vclr_c32_4op_p (vcoefRes2, vcoefRes3, vcoefRes4, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vclr_c32_4op_p version.


Main table → Move And Pack → Clear → Vector Clear
Intrinsic     vclr_v32[_p]
name
Spec syntax   vclr {Oop} vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8        1..8   Number of atomic operations
Operands
              2    IN_VPR          vprex_t             Vector predicate operand
              vec_t vRes;
              vprex_t vecPred;
C example     ...
              vRes = vclr_v32_p (8, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vclr_v32_p version.


Main table → Move And Pack → Clear → Vector Clear
