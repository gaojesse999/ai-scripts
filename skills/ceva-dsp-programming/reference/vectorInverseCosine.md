# Special Algorithms → Inverse Cosine Squared → Vector Inverse Cosine

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Special Algorithms → Inverse Cosine Squared → Vector Inverse Cosine
Squared

Vector Inverse Cosine Squared

Vector Inverse Cosine Squared
Performs two linear piece wise estimations on two sources. The multiplicand and addend are
obtained from a fixed table. The sources are a 16-bit real signed positive numbers. The
destinations are 16-bit signed numbers.
Available Switches

Number of atomic operations. An atomic operation is defined as two linear piece wise
Hhop
           estimations on two source. Writes to a vector destination. 9op ≤ Hhop ≤ 16op
           Number of atomic operations. An atomic operation is defined as two linear piece wise
Oop
           estimations on two source. Writes to a vector destination. 1op ≤ Oop ≤ 8op
Intrinsic Names
vacossq_v32_v32_v32_v32
vacossq_v32_v32
Instruction details in the instruction set specification
Intrinsic     vacossq_v32_v32_v32_v32[_p]
name
Spec syntax   vacossq {Hhop} vx[0], vy[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    HHOP           uint8     9..16            Number of atomic operations
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
              vRes1 = vacossq_v32_v32_v32_v32_p (16, vIn, vIn2, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vacossq_v32_v32_v32_v32_p
              1.
                   version.
                   This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).
Comments
                   The vacossq_v32_v32_v32_v32_p intrinsic has different latency in case the
                   Demapper block is installed/not installed on the HW. When Demapper is not
                   installed, 1/2 cycles are added after the generated vector instruction. The SDT
              3.
                   default is "Demapper installed". Therefore, for ensuring correct execution on
                   the HW, the -mno-demapper Compiler switch must be specified in case
                   Demapper is not installed.


Main table → Special Algorithms → Inverse Cosine Squared → Vector Inverse Cosine
Squared
Intrinsic     vacossq_v32_v32[_p]
name
Spec syntax   vacossq {Oop} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8           Number of atomic operations

Operands      2    IN1_V32         vec_t                    Input vector operand
              3    IN_VPR          vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vacossq_v32_v32_p (8, vIn, vecPred);

              1.   IN_VPR last operand is relevant only for vacossq_v32_v32_p version.
                   The vacossq_v32_v32_p intrinsic has different latency in case the Demapper
                   block is installed/not installed on the HW. When Demapper is not installed,
Comments           1/2 cycles are added after the generated vector instruction. The SDT default is
              2.
                   "Demapper installed". Therefore, for ensuring correct execution on the HW,
                   the -mno-demapper Compiler switch must be specified in case Demapper is
                   not installed.


Main table → Special Algorithms → Inverse Cosine Squared → Vector Inverse Cosine
Squared
