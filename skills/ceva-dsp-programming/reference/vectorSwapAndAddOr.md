# Arithmetic → Swap and Add or Subtract → Vector Swap and Add or

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract

Vector Swap and Add or Subtract

Vector Swap and Add or Subtract
Performs swap between two 32-bit sources and addition/subtraction operation. Each operation is
between two sources into destination. The sources and the destination are either 32-bit or 40-bit
wide determined by the vector register type.
Available Switches
          Number of atomic operations. An atomic operation is defined as a pair of asu operations.
Qop
          1op ≤ Qop ≤ 4op
mm        Performs two subtractions. The default behavior is two additions.
mp        Perform subtraction first and then addition. The default behavior is two additions.

pm        Perform addition first and then subtraction. The default behavior is two additions.
Intrinsic Names
vswas_v32_v32_v32_mm
vswas_v32_v32_v32_mp
vswas_v32_v32_v32
vswas_v32_v32_v32_pm
Instruction details in the instruction set specification
Intrinsic     vswas_v32_v32_v32_mm[_p]
name
Spec syntax   vswas {Qop [,pm_mp_mm]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vswas_v32_v32_v32_mm_p (4, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vswas_v32_v32_v32_mm_p
Comments      1.
                   version.


Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract
Intrinsic     vswas_v32_v32_v32_mp[_p]
name
Spec syntax   vswas {Qop [,pm_mp_mm]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vswas_v32_v32_v32_mp_p (4, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vswas_v32_v32_v32_mp_p
Comments      1.
                   version.


Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract
Intrinsic     vswas_v32_v32_v32[_p]
name
Spec syntax   vswas {Qop [,pm_mp_mm]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_V32         vec_t                      Input vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand

vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vswas_v32_v32_v32_p (4, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vswas_v32_v32_v32_p version.


Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract
Intrinsic     vswas_v32_v32_v32_pm[_p]
name
Spec syntax   vswas {Qop [,pm_mp_mm]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8     1..4             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_V32         vec_t                      Input vector operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vswas_v32_v32_v32_pm_p (4, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vswas_v32_v32_v32_pm_p
Comments      1.
                   version.


Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract

Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract Word Parts

Vector Swap and Add or Subtract Word Parts

Vector Swap and Add or Subtract Word Parts
Performs swap between two 16-bit sources and addition/subtraction operation. Each operation is
between two sources into destination. The sources and the destination are either 16-bit or 20-bit
wide and are packed into either 32-bit or 40-bit destination determined by the vector register
type.
Available Switches
           Number of atomic operations. An atomic operation is defined as a pair of asu
Oop
           operations. 1op ≤ Oop ≤ 8op
mm         Performs two subtractions. The default behavior is two additions.
mp         Perform subtraction first and then addition. The default behavior is two additions.
pm         Perform addition first and then subtraction. The default behavior is two additions.
Intrinsic Names
vswasw_v32_v32_v32_v32_mm
vswasw_v32_v32_v32_v32_mp
vswasw_v32_v32_v32_v32
vswasw_v32_v32_v32_v32_pm
vswasw_v32_v32_v32_mm
vswasw_v32_v32_v32_mp
vswasw_v32_v32_v32
vswasw_v32_v32_v32_pm
Instruction details in the instruction set specification
Intrinsic     vswasw_v32_v32_v32_v32_mm[_p]
name

Spec syntax   vswasw {Oop [,pm_mp_mm]} vx[0], vy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands      3    IN2_V32        vec_t                     Input vector operand
              4    RES2_V32       vec_t                     Input vector result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vswasw_v32_v32_v32_v32_mm_p (8, vIn, vIn2, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vswasw_v32_v32_v32_v32_mm_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract Word Parts
Intrinsic     vswasw_v32_v32_v32_v32_mp[_p]
name
Spec syntax   vswasw {Oop [,pm_mp_mm]} vx[0], vy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands      3    IN2_V32        vec_t                     Input vector operand
              4    RES2_V32       vec_t                     Input vector result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vswasw_v32_v32_v32_v32_mp_p (8, vIn, vIn2, vRes2, vecPred);
                   IN_VPR last operand is relevant only for vswasw_v32_v32_v32_v32_mp_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).

Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract Word Parts
Intrinsic     vswasw_v32_v32_v32_v32[_p]
name
Spec syntax   vswasw {Oop [,pm_mp_mm]} vx[0], vy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN2_V32        vec_t                      Input vector operand
              4    RES2_V32       vec_t                      Input vector result operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes1;
C example     vec_t vRes2;
              vprex_t vecPred;
              ...
              vRes1 = vswasw_v32_v32_v32_v32_p (8, vIn, vIn2, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vswasw_v32_v32_v32_v32_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract Word Parts
Intrinsic     vswasw_v32_v32_v32_v32_pm[_p]
name
Spec syntax   vswasw {Oop [,pm_mp_mm]} vx[0], vy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN2_V32        vec_t                      Input vector operand
            4    RES2_V32       vec_t                     Input vector result operand
            5    IN_VPR         vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vIn2;
            vec_t vRes1;
C example   vec_t vRes2;
            vprex_t vecPred;
            ...
            vRes1 = vswasw_v32_v32_v32_v32_pm_p (8, vIn, vIn2, vRes2, vecPred);

                 IN_VPR last operand is relevant only for vswasw_v32_v32_v32_v32_pm_p
            1.
                 version.
Comments         This intrinsic returns two results. The first result variable should be placed to
            2.   the left of the = sign (lvalue). The second result variable should be passed as

an additional parameter (RES2_V32).


Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract Word Parts
Intrinsic     vswasw_v32_v32_v32_mm[_p]
name
Spec syntax   vswasw {Oop [,pm_mp_mm]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vswasw_v32_v32_v32_mm_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vswasw_v32_v32_v32_mm_p
Comments      1.
                   version.


Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract Word Parts
Intrinsic     vswasw_v32_v32_v32_mp[_p]
name
Spec syntax   vswasw {Oop [,pm_mp_mm]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands
              3    IN2_V32        vec_t                     Input vector operand
              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vswasw_v32_v32_v32_mp_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vswasw_v32_v32_v32_mp_p
Comments      1.
                   version.


Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract Word Parts
Intrinsic     vswasw_v32_v32_v32[_p]
name
Spec syntax   vswasw {Oop [,pm_mp_mm]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands
              3    IN2_V32        vec_t                      Input vector operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;

C example     vprex_t vecPred;
              ...
              vRes = vswasw_v32_v32_v32_p (8, vIn, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vswasw_v32_v32_v32_p version.


Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract Word Parts
Intrinsic     vswasw_v32_v32_v32_pm[_p]
name
Spec syntax   vswasw {Oop [,pm_mp_mm]} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands
              3    IN2_V32        vec_t                      Input vector operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vswasw_v32_v32_v32_pm_p (8, vIn, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vswasw_v32_v32_v32_pm_p
Comments      1.
                   version.


Main table → Arithmetic → Swap and Add or Subtract → Vector Swap and Add or
Subtract Word Parts
