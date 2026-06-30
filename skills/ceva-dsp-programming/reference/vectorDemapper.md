# Special Algorithms → Demapper → Vector Demapper

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Special Algorithms → Demapper → Vector Demapper

Vector Demapper

Vector Demapper
Performs linear piece wise estimation on source, according to defined modulation. The
multiplicand and addend are obtained from a fixed look-up table. The source is a 16-bit complex
signed number (16-bit real and 16-bit imaginary). The result is 16-bit wide or 20-bit wide signed
number, determined by the vector register type.
Available Switches
             Number of atomic operations. An atomic operation is defined as a linear piece wise
Dop
             estimation on one source. Writes to one vector destination. 1op ≤ Dop ≤ 2op
             Number of atomic operations. An atomic operation is defined as a linear piece wise
Ohop
             estimation on one source. Writes to one vector destination. 5op ≤ Ohop ≤ 8op

Number of atomic operations. An atomic operation is defined as a linear piece wise
Oop
             estimation on one source. Writes to one vector destination. 1op ≤ Oop ≤ 8op
             Number of atomic operations. An atomic operation is defined as a linear piece wise
Qhop
             estimation on one source. Writes to one vector destination. 3op ≤ Qhop ≤ 4op
             Number of atomic operations. An atomic operation is defined as a linear piece wise
Qop
             estimation on one source. Writes to one vector destination. 1op ≤ Qop ≤ 4op
             Each modulation accesses a dedicated look-up table and outputs a different number of
Xpsk
             results per source:
             When used, bpsk modulation accesses a dedicated look-up table and outputs 1 results
bpsk
             per input
             Each modulation accesses a dedicated look-up table and outputs a different number of
qamX
             results per source:
Intrinsic Names
vdemap_v32_v32_v32_qam16
vdemap_v32_v32_qam16
vdemap_v32_v32_v32_qam256
vdemap_v32_v32_v32_qam64
vdemap_v32_v32_bpsk
vdemap_v32_v32_qpsk
vdemap_v32_v32_qam256
vdemap_v32_v32_qam64
Instruction details in the instruction set specification
Intrinsic     vdemap_v32_v32_v32_qam16[_p]
name
Spec syntax   vdemap {Ohop, qam16} vx[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    OHOP           uint8     5..8           Number of atomic operations
              2    IN1_V32        vec_t                    Input vector operand
Operands
              3    RES2_V32       vec_t                    Input vector result operand
              4    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vdemap_v32_v32_v32_qam16_p (8, vIn, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vdemap_v32_v32_v32_qam16_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Special Algorithms → Demapper → Vector Demapper
Intrinsic     vdemap_v32_v32_qam16[_p]
name
Spec syntax   vdemap {Qop, qam16} vx[0], vz[0], ?vprX

Return type   vec_t

1    QOP            uint8     1..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands                                                    Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                            2

              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vdemap_v32_v32_qam16_p (4, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vdemap_v32_v32_qam16_p
Comments      1.
                   version.


Main table → Special Algorithms → Demapper → Vector Demapper
Intrinsic     vdemap_v32_v32_v32_qam256[_p]
name
Spec syntax   vdemap {Qhop, qam256_qam64} vx[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    QHOP           uint8     3..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

Operands      3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    RES2_V32       vec_t                     Input vector result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vdemap_v32_v32_v32_qam256_p (4, vIn, 0, vRes2, vecPred);

                   IN_VPR last operand is relevant only for vdemap_v32_v32_v32_qam256_p
              1.
                   version.
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V32).


Main table → Special Algorithms → Demapper → Vector Demapper
Intrinsic     vdemap_v32_v32_v32_qam64[_p]
name
Spec syntax   vdemap {Qhop, qam256_qam64} vx[0], vz1[0], vz2[0], ?vprX

Return type   vec_t

              1    QHOP           uint8     3..4            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand

Operands      3    IN1_OFST       uint8     0,4
                                                            Offset for the first DW used from operand
                                                            2

              4    RES2_V32       vec_t                     Input vector result operand
              5    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes1;
              vec_t vRes2;
C example     vprex_t vecPred;
              ...
              vRes1 = vdemap_v32_v32_v32_qam64_p (4, vIn, 0, vRes2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vdemap_v32_v32_v32_qam64_p
                 version.
                 This intrinsic returns two results. The first result variable should be placed to
            2.   the left of the = sign (lvalue). The second result variable should be passed as
                 an additional parameter (RES2_V32).


Main table → Special Algorithms → Demapper → Vector Demapper
Intrinsic     vdemap_v32_v32_bpsk[_p]
name
Spec syntax   vdemap {Oop, bpsk} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands                                                     Offset for the first DW used from the
              3    OUT_OFST       uint8     0,4
                                                             result operand
              4    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vdemap_v32_v32_bpsk_p (8, vIn, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vdemap_v32_v32_bpsk_p version.


Main table → Special Algorithms → Demapper → Vector Demapper
Intrinsic     vdemap_v32_v32_qpsk[_p]
name
Spec syntax   vdemap {Oop, qpsk} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vdemap_v32_v32_qpsk_p (8, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vdemap_v32_v32_qpsk_p version.


Main table → Special Algorithms → Demapper → Vector Demapper
Intrinsic     vdemap_v32_v32_qam256[_p]
name
Spec syntax   vdemap {Dop, qam256_qam64} vx[0], vz[0], ?vprX

Return type   vec_t

              1    DOP            uint8     1..2            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands                                                    Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                            2

              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vdemap_v32_v32_qam256_p (2, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vdemap_v32_v32_qam256_p
Comments      1.
                   version.


Main table → Special Algorithms → Demapper → Vector Demapper
Intrinsic     vdemap_v32_v32_qam64[_p]
name
Spec syntax   vdemap {Dop, qam256_qam64} vx[0], vz[0], ?vprX

Return type   vec_t

              1    DOP            uint8     1..2            Number of atomic operations
              2    IN1_V32        vec_t                     Input vector operand
Operands                                                    Offset for the first DW used from operand
              3    IN1_OFST       uint8     0,4
                                                            2

              4    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vdemap_v32_v32_qam64_p (2, vIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vdemap_v32_v32_qam64_p
Comments      1.
                   version.


Main table → Special Algorithms → Demapper → Vector Demapper
