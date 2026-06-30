# Arithmetic → Add and Subtract → Vector Add and Subtract 16-bit Word

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Arithmetic → Add and Subtract → Vector Add and Subtract 16-bit Word
Parts

Vector Add and Subtract 16-bit Word Parts

Vector Add and Subtract 16-bit Word Parts
Performs two additions and two subtractions. Each addition and subtraction is between the same
two sources. The sum and difference are stored in the destination registers. The sources are 16-
bit and the results are 16-bit wide and are packed into a 32-bit or 40-bit destination.
Available Switches
           Number of atomic operations. An atomic operation is defined as two additions and two
Oop
           subtractions.
Intrinsic Names
vaddsub16_v32_v32_v32_v32
Instruction details in the instruction set specification
Intrinsic     vaddsub16_v32_v32_v32_v32[_p]
name
Spec syntax   vaddsub16 {Oop} vx[0], vy[0], vz1[0], vz2[0], ?vprX

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
              vRes1 = vaddsub16_v32_v32_v32_v32_p (8, vIn, vIn2, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vaddsub16_v32_v32_v32_v32_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Arithmetic → Add and Subtract → Vector Add and Subtract 16-bit Word
Parts
