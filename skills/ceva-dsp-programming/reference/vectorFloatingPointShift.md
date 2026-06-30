# Floating Point → Float Special Operations → Vector Floating Point Shift

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Special Operations → Vector Floating Point Shift
Add/Sub

Vector Floating Point Shift Add/Sub

Vector Floating Point Shift Add/Sub
Performs a subtraction/addition between the mantissas of two sources in 32-bit single precision
floating point format and determines the sign of the final floating point result. The mantissa of
the smaller source (in absolute value) is shifted according to the delta between the two

exponents, and than subtracted/added from the mantissa of the larger source. This instruction is
part of the non-native VFLPADD, VFLPSUB operations.
Available Switches
None
Intrinsic Names
vflpshasu_v32_v32_vpr_v32_fadd
vflpshasu_v32_v32_vpr_v32_fsub
Instruction details in the instruction set specification
Intrinsic     vflpshasu_v32_v32_vpr_v32_fadd[_p]
name
Spec syntax   vflpshasu {Oop, fadd_fsub} vx[0], vy[0], VPREX, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
Operands      3    IN2_V32         vec_t                     Input vector operand
              4    RES2_VPR        vprex_t                   Vector predicate result operand
              5    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              vprex_t vecPredRes;
              ...
              vRes = vflpshasu_v32_v32_vpr_v32_fadd_p (8, vIn, vIn2, vecPredRes, vecPred);

                   IN_VPR last operand is relevant only for
              1.
                   vflpshasu_v32_v32_vpr_v32_fadd_p version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VPR).


Main table → Floating Point → Float Special Operations → Vector Floating Point Shift
Add/Sub
Intrinsic     vflpshasu_v32_v32_vpr_v32_fsub[_p]
name
Spec syntax   vflpshasu {Oop, fadd_fsub} vx[0], vy[0], VPREX, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
Operands      3    IN2_V32         vec_t                     Input vector operand
              4    RES2_VPR        vprex_t                   Vector predicate result operand
              5    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              vprex_t vecPredRes;
              ...
              vRes = vflpshasu_v32_v32_vpr_v32_fsub_p (8, vIn, vIn2, vecPredRes, vecPred);

IN_VPR last operand is relevant only for
             1.
                  vflpshasu_v32_v32_vpr_v32_fsub_p version.
Comments          This intrinsic returns two results. The first result variable should be placed to
             2.   the left of the = sign (lvalue). The second result variable should be passed as
                  an additional parameter (RES2_VPR).


Main table → Floating Point → Float Special Operations → Vector Floating Point Shift
Add/Sub
