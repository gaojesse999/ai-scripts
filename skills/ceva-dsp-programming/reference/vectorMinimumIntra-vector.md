# Intra Vector → Minimum Intra-Vector → Vector Minimum Intra-Vector

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Intra Vector → Minimum Intra-Vector → Vector Minimum Intra-Vector

Vector Minimum Intra-Vector

Vector Minimum Intra-Vector
Performs an intra-vector minimum operation between sources that are located in the same vector.
Each source is 32-bit wide. The destination is 32-bit wide or 40-bit wide determined by the
vector register type.
Available Switches
         Number of atomic operations. An atomic operation is defined by a single comparison. 1op
Qop
         ≤ Qop ≤ 4op
         When used, the sources represented by the 32-bits of the vector part are treated as
uu
         unsigned values (by default they are treated as signed values).
Intrinsic Names
vminint_v32_c32_v32
vminint_v32_c32_v32_uu
Instruction details in the instruction set specification
Intrinsic     vminint_v32_c32_v32[_p]
name
Spec syntax   vminint {Qop [,uu]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4              Number of atomic operations
              2    IN1_V32        vec_t                       Input vector operand
Operands      3    IN2_C32        coef_t                      Coefficient operand

4    IN2_PART       uint8     LOW,HIGH          Word part which is used for operand 3
              5    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vminint_v32_c32_v32_p (4, vIn, vcoefIn, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vminint_v32_c32_v32_p version.


Main table → Intra Vector → Minimum Intra-Vector → Vector Minimum Intra-Vector
Intrinsic     vminint_v32_c32_v32_uu[_p]
name
Spec syntax   vminint {Qop [,uu]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4              Number of atomic operations
              2    IN1_V32        vec_t                       Input vector operand
Operands      3    IN2_C32        coef_t                      Coefficient operand
              4    IN2_PART       uint8     LOW,HIGH          Word part which is used for operand 3
              5    IN_VPR         vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vminint_v32_c32_v32_uu_p (4, vIn, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vminint_v32_c32_v32_uu_p
Comments      1.
                   version.


Main table → Intra Vector → Minimum Intra-Vector → Vector Minimum Intra-Vector

Main table → Intra Vector → Minimum Intra-Vector → Vector Minimum Intra-Vector
Word

Vector Minimum Intra-Vector Word

Vector Minimum Intra-Vector Word
Performs an intra-vector minimum operation between sources that are located in the same vector.
Each source is 16-bit wide. The destination is 16-bit wide or 20-bit wide determined by the
vector register type.
Available Switches
         Number of atomic operations. An atomic operation is defined by a single comparison. 1op
Oop
         ≤ Oop ≤ 8op
         When used, the sources represented by the 16-bits of the vector part are treated as
uu
         unsigned values (by default they are treated as signed values).
Intrinsic Names
vminintw_v32_c32_v32
vminintw_v32_c32_v32_uu
Instruction details in the instruction set specification
Intrinsic     vminintw_v32_c32_v32[_p]
name
Spec syntax   vminintw {Oop [,uu]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands      3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vminintw_v32_c32_v32_p (8, vIn, vcoefIn, LOW, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vminintw_v32_c32_v32_p version.


Main table → Intra Vector → Minimum Intra-Vector → Vector Minimum Intra-Vector
Word
Intrinsic     vminintw_v32_c32_v32_uu[_p]
name
Spec syntax   vminintw {Oop [,uu]} vx[0], vcYp, vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands      3    IN2_C32        coef_t                    Coefficient operand
              4    IN2_PART       uint8     LOW,HIGH        Word part which is used for operand 3
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vminintw_v32_c32_v32_uu_p (8, vIn, vcoefIn, LOW, vecPred);

                   IN_VPR last operand is relevant only for vminintw_v32_c32_v32_uu_p
Comments      1.
                   version.


Main table → Intra Vector → Minimum Intra-Vector → Vector Minimum Intra-Vector
Word
