# Move And Pack → Move → Vector Move VM

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → Move → Vector Move VM

Vector Move VM

Vector Move VM
Performs data move from source to destination. The source is 40-bit wide and destination is
either 32-bit or 40-bit wide determined by the vector register type.
Available Switches
             Number of atomic operations. An atomic operation is defined as a single move
Oop
             operation. 1op ≤ Oop ≤ 8op
             Number of atomic operations. An atomic operation is defined as a single move
Qop
             operation. 1op ≤ Qop ≤ 4op
             Pseudo-switch which is replaced by >>8, when used, the data is pre-shifted to the right
SHFR8
             by 8. The shift type is arithmetic.
Intrinsic Names
vmovm_v40_v32_SHFR8
vmovm_v40_v32
vmovm_v40_c32_1op
vmovm_v40_c32_2op
vmovm_v40_c32_3op
vmovm_v40_c32_4op
Instruction details in the instruction set specification
Intrinsic     vmovm_v40_v32_SHFR8[_p]
name

Spec syntax   vmovm {Oop [,SHFR8]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8               Number of atomic operations
              2    IN1_V40         vec40_t                      Output vector operand

              3    IN1_OFST        uint8     0,4
                                                                Offset for the first DW used from operand
Operands                                                        2

                                                                Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                                result operand
              5    IN_VPR          vprex_t                      Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmovm_v40_v32_SHFR8_p (8, vIn, 0, 0, vecPred);

                   IN_VPR last operand is relevant only for vmovm_v40_v32_SHFR8_p
Comments      1.
                   version.


Main table → Move And Pack → Move → Vector Move VM
Intrinsic     vmovm_v40_v32[_p]
name
Spec syntax   vmovm {Oop [,SHFR8]} vox[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8               Number of atomic operations
              2    IN1_V40         vec40_t                      Output vector operand

              3    IN1_OFST        uint8     0,4
                                                                Offset for the first DW used from operand
Operands                                                        2

                                                                Offset for the first DW used from the
              4    OUT_OFST        uint8     0,4
                                                                result operand
              5    IN_VPR          vprex_t                      Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vmovm_v40_v32_p (8, vIn, 0, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovm_v40_v32_p version.


Main table → Move And Pack → Move → Vector Move VM
Intrinsic     vmovm_v40_c32_1op[_p]
name
Spec syntax   vmovm {Qop} vox[0], vc0, ?vprX

Return type   coef_t

              1    IN1_V40        vec40_t                   Output vector operand

Operands      2    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            1

              3    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vIn;
              coef_t vcoefRes;
C example     vprex_t vecPred;
              ...
              vcoefRes = vmovm_v40_c32_1op_p (vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vmovm_v40_c32_1op_p version.


Main table → Move And Pack → Move → Vector Move VM
Intrinsic     vmovm_v40_c32_2op[_p]
name
Spec syntax   vmovm {Qop} vox[0], vc0, ?vprX

Return type   coef_t

              1    IN1_V40        vec40_t                   Output vector operand

              2    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            1
Operands
                                                            Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                            expected)
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vIn;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     vprex_t vecPred;
              ...
              vcoefRes1 = vmovm_v40_c32_2op_p (vIn, 0, vcoefRes2, vecPred);

              1.   IN_VPR last operand is relevant only for vmovm_v40_c32_2op_p version.

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Move And Pack → Move → Vector Move VM
Intrinsic     vmovm_v40_c32_3op[_p]
name
Spec syntax   vmovm {Qop} vox[0], vc0, ?vprX

Return type   coef_t

              1    IN1_V40        vec40_t                   Output vector operand

              2    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            1

                                                            Coefficient result operand (register vc1 is
Operands      3    RES2_VC1       coef_t

expected)
                                                            Coefficient result operand (register vc2 is
              4    RES3_VC2       coef_t
                                                            expected)
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vIn;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              vprex_t vecPred;
              ...
              vcoefRes1 = vmovm_v40_c32_3op_p (vIn, 0, vcoefRes2, vcoefRes3, vecPred);

              1.   IN_VPR last operand is relevant only for vmovm_v40_c32_3op_p version.

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Move And Pack → Move → Vector Move VM
Intrinsic     vmovm_v40_c32_4op[_p]
name
Spec syntax   vmovm {Qop} vox[0], vc0, ?vprX

Return type   coef_t

              1    IN1_V40        vec40_t                   Output vector operand

              2    IN1_OFST       uint8     0,4             Offset for the first DW used from operand
                                                            1

                                                            Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                            expected)
Operands
              4
                                                            Coefficient result operand (register vc2 is
                   RES3_VC2       coef_t
                                                            expected)
                                                            Coefficient result operand (register vc3 is
              5    RES4_VC3       coef_t
                                                            expected)
              6    IN_VPR         vprex_t                   Vector predicate operand
              vec40_t vIn;
C example     coef_t vcoefRes1;
              coef_t vcoefRes2;
           coef_t vcoefRes3;
           coef_t vcoefRes4;
           vprex_t vecPred;
           ...
           vcoefRes1 = vmovm_v40_c32_4op_p (vIn, 0, vcoefRes2, vcoefRes3, vcoefRes4, vecPred);

           1.   IN_VPR last operand is relevant only for vmovm_v40_c32_4op_p version.

Comments        This intrinsic returns more than one result. The first result variable should be
           2.   placed to the left of the = sign (lvalue). Additional result variables should be
                passed as parameters.


Main table → Move And Pack → Move → Vector Move VM
