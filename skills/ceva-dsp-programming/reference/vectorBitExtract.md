# Bit Manipulation → Bit Extract → Vector Bit Extract

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Bit Extract → Vector Bit Extract

Vector Bit Extract

Vector Bit Extract
Performs extraction of bits according to a given width and offset from a source into a destination.
The width represents the number of bits to be extracted from the source; the offset represents the
number of bits from the beginning of the source. The source is 32-bit wide. The destination is
32-bit wide.
Available Switches

Number of atomic operations. An atomic operation is defined as a single extraction
Oop
           operation. 1op ≤ Oop ≤ 8op
b          Offset values are given by bytes
dw         Offset values are given by double-words
nib        Nibbles are read from the source
           When used, the rest of each destination which is written is zero-extended. The default is
u
           sign-extended.
w          Offset values are given by words
Intrinsic Names
vbextract_v32_c32_v32_v32_w
vbextract_v32_c32_v32_v32_w_u
vbextract_v32_width6_offset5_v32
vbextract_v32_width6_offset5_v32_u
vbextract_v32_width6_v32_v32_w
vbextract_v32_width6_v32_v32_w_u
vbextract_v32_c32_v32_nib
vbextract_v32_c32_v32
vbextract_v32_c32_v32_u
vbextract_v32_offset4_v32_nib
vbextract_v32_width6_v32_v32_dw
vbextract_v32_width6_v32_v32_dw_u
vbextract_v32_c32_v32_v32_b
vbextract_v32_c32_v32_v32_b_u
vbextract_v32_c32_v32_v32_dw
vbextract_v32_c32_v32_v32_dw_u
vbextract_v32_width6_v32_v32_b
vbextract_v32_width6_v32_v32_b_u
Instruction details in the instruction set specification
Intrinsic     vbextract_v32_c32_v32_v32_w[_p]
name
Spec syntax   vbextract {Oop, w [,u]} vx[0], vcYp, vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand

Operands
              4    IN2_PART        uint8     LOW,HIGH        Word part which is used for operand 3
              5    IN3_V32         vec_t                     Input vector operand

              6    IN3_OFST        uint8     0,4             Offset for the first DW used from operand
                                                             5

              7    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vbextract_v32_c32_v32_v32_w_p (8, vIn, vcoefIn, LOW, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vbextract_v32_c32_v32_v32_w_p
Comments      1.
                   version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_c32_v32_v32_w_u[_p]
name
Spec syntax   vbextract {Oop, w [,u]} vx[0], vcYp, vy[0], vz[0], ?vprX

Return type   vec_t

1    OOP             uint8     1..8            Number of atomic operations
              2    IN1_V32         vec_t                     Input vector operand
              3    IN2_C32         coef_t                    Coefficient operand

Operands
              4    IN2_PART        uint8     LOW,HIGH        Word part which is used for operand 3
              5    IN3_V32         vec_t                     Input vector operand

              6    IN3_OFST        uint8     0,4             Offset for the first DW used from operand
                                                             5

              7    IN_VPR          vprex_t                   Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vRes;
             coef_t vcoefIn;
             vprex_t vecPred;
             ...
             vRes = vbextract_v32_c32_v32_v32_w_u_p (8, vIn, vcoefIn, LOW, vIn2, 0, vecPred);

                  IN_VPR last operand is relevant only for
Comments     1.
                  vbextract_v32_c32_v32_v32_w_u_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_width6_offset5_v32[_p]
name
Spec syntax   vbextract {Oop [,u]} vx[0], #width6, #offset5, vz[0], ?vprX

Return type   vec_t

              1    OOP              uint8     1..8             Number of atomic operations
              2    IN1_V32          vec_t                      Input vector operand
Operands      3    IN2_WIDTH6       int16     0..63            6 bit unsigned immediate
              4    IN3_OFFSET5 int16          0..31            5 bit unsigned immediate
              5    IN_VPR           vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbextract_v32_width6_offset5_v32_p (8, vIn, 2, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vbextract_v32_width6_offset5_v32_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_width6_offset5_v32_u[_p]
name
Spec syntax   vbextract {Oop [,u]} vx[0], #width6, #offset5, vz[0], ?vprX

Return type   vec_t

              1    OOP              uint8     1..8             Number of atomic operations
              2    IN1_V32          vec_t                      Input vector operand

Operands      3    IN2_WIDTH6       int16     0..63            6 bit unsigned immediate
              4    IN3_OFFSET5 int16          0..31            5 bit unsigned immediate
              5    IN_VPR           vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbextract_v32_width6_offset5_v32_u_p (8, vIn, 2, 2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vbextract_v32_width6_offset5_v32_u_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_width6_v32_v32_w[_p]
name
Spec syntax   vbextract {Oop, w [,u]} vx[0], #width6, vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
              3    IN2_WIDTH6 int16          0..63            6 bit unsigned immediate
Operands      4    IN3_V32         vec_t                      Input vector operand

              5    IN3_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbextract_v32_width6_v32_v32_w_p (8, vIn, 2, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vbextract_v32_width6_v32_v32_w_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_width6_v32_v32_w_u[_p]
name
Spec syntax   vbextract {Oop, w [,u]} vx[0], #width6, vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
              3    IN2_WIDTH6 int16          0..63            6 bit unsigned immediate
Operands      4    IN3_V32         vec_t                      Input vector operand

              5    IN3_OFST        uint8     0,4              Offset for the first DW used from operand
                                                              4

6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbextract_v32_width6_v32_v32_w_u_p (8, vIn, 2, vIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for
                vbextract_v32_width6_v32_v32_w_u_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_c32_v32_nib[_p]
name
Spec syntax   vbextract {nib} vx[0], vcY, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t                      Input vector operand
              2    IN2_C32         coef_t                     Coefficient operand
Operands                                                      Offset for the first DW used from the
              3    OUT_OFST        uint8     0,4
                                                              result operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vbextract_v32_c32_v32_nib_p (vIn, vcoefIn, 0, vecPred);

                   IN_VPR last operand is relevant only for vbextract_v32_c32_v32_nib_p
Comments      1.
                   version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_c32_v32[_p]
name
Spec syntax   vbextract {Oop [,u]} vx[0], vcY, vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_C32         coef_t                     Coefficient operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vbextract_v32_c32_v32_p (8, vIn, vcoefIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vbextract_v32_c32_v32_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_c32_v32_u[_p]
name
Spec syntax   vbextract {Oop [,u]} vx[0], vcY, vz[0], ?vprX

Return type   vec_t

1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
Operands
              3    IN2_C32         coef_t                     Coefficient operand
              4    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
              coef_t vcoefIn;
C example     vprex_t vecPred;
              ...
              vRes = vbextract_v32_c32_v32_u_p (8, vIn, vcoefIn, vecPred);

                   IN_VPR last operand is relevant only for vbextract_v32_c32_v32_u_p
Comments      1.
                   version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_offset4_v32_nib[_p]
name
Spec syntax   vbextract {nib} vx[0], #offset4, vz[0], ?vprX

Return type   vec_t

              1    IN1_V32          vec_t                      Input vector operand
              2    IN2_OFFSET4 int16          0..15            4 bit unsigned immediate
Operands                                                       Offset for the first DW used from the
              3    OUT_OFST         uint8     0,2
                                                               result operand
              4    IN_VPR           vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbextract_v32_offset4_v32_nib_p (vIn, 2, 0, vecPred);

                   IN_VPR last operand is relevant only for vbextract_v32_offset4_v32_nib_p
Comments      1.
                   version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_width6_v32_v32_dw[_p]
name
Spec syntax   vbextract {Oop, dw [,u]} vx[0], #width6, vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN2_WIDTH6 int16         0..63            6 bit unsigned immediate
              4    IN3_V32        vec_t                      Input vector operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...

vRes = vbextract_v32_width6_v32_v32_dw_p (8, vIn, 2, vIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vbextract_v32_width6_v32_v32_dw_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_width6_v32_v32_dw_u[_p]
name
Spec syntax   vbextract {Oop, dw [,u]} vx[0], #width6, vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
Operands      3    IN2_WIDTH6 int16         0..63            6 bit unsigned immediate
              4    IN3_V32        vec_t                      Input vector operand
              5    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbextract_v32_width6_v32_v32_dw_u_p (8, vIn, 2, vIn2, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vbextract_v32_width6_v32_v32_dw_u_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_c32_v32_v32_b[_p]
name
Spec syntax   vbextract {Oop, b [,u]} vx[0], vcYp, vy[Ye], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand

Operands
              4    IN2_PART        uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN3_V32         vec_t                      Input vector operand

              6    IN3_OFST        uint8     0,2,4,6          Offset for the first DW used from operand
                                                              5

              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vbextract_v32_c32_v32_v32_b_p (8, vIn, vcoefIn, LOW, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for vbextract_v32_c32_v32_v32_b_p
Comments      1.

version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_c32_v32_v32_b_u[_p]
name
Spec syntax   vbextract {Oop, b [,u]} vx[0], vcYp, vy[Ye], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
              3    IN2_C32         coef_t                     Coefficient operand

Operands
              4    IN2_PART        uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN3_V32         vec_t                      Input vector operand

              6    IN3_OFST        uint8     0,2,4,6          Offset for the first DW used from operand
                                                              5

              7    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
C example     vec_t vIn2;
              vec_t vRes;
             coef_t vcoefIn;
             vprex_t vecPred;
             ...
             vRes = vbextract_v32_c32_v32_v32_b_u_p (8, vIn, vcoefIn, LOW, vIn2, 0, vecPred);

                  IN_VPR last operand is relevant only for
Comments     1.
                  vbextract_v32_c32_v32_v32_b_u_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_c32_v32_v32_dw[_p]
name
Spec syntax   vbextract {Oop, dw [,u]} vx[0], vcYp, vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
Operands
              4    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN3_V32        vec_t                      Input vector operand
              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vbextract_v32_c32_v32_v32_dw_p (8, vIn, vcoefIn, LOW, vIn2, vecPred);

                   IN_VPR last operand is relevant only for vbextract_v32_c32_v32_v32_dw_p
Comments      1.
                   version.

Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_c32_v32_v32_dw_u[_p]
name
Spec syntax   vbextract {Oop, dw [,u]} vx[0], vcYp, vy[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8             Number of atomic operations
              2    IN1_V32        vec_t                      Input vector operand
              3    IN2_C32        coef_t                     Coefficient operand
Operands
              4    IN2_PART       uint8     LOW,HIGH         Word part which is used for operand 3
              5    IN3_V32        vec_t                      Input vector operand
              6    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     coef_t vcoefIn;
              vprex_t vecPred;
              ...
              vRes = vbextract_v32_c32_v32_v32_dw_u_p (8, vIn, vcoefIn, LOW, vIn2, vecPred);

Comments      1.   IN_VPR last operand is relevant only for
                vbextract_v32_c32_v32_v32_dw_u_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_width6_v32_v32_b[_p]
name
Spec syntax   vbextract {Oop, b [,u]} vx[0], #width6, vy[Ye], vz[0], ?vprX

Return type   vec_t

              1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
              3    IN2_WIDTH6 int16          0..63            6 bit unsigned immediate
Operands      4    IN3_V32         vec_t                      Input vector operand

              5    IN3_OFST        uint8     0,2,4,6          Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbextract_v32_width6_v32_v32_b_p (8, vIn, 2, vIn2, 0, vecPred);

                   IN_VPR last operand is relevant only for
Comments      1.
                   vbextract_v32_width6_v32_v32_b_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
Intrinsic     vbextract_v32_width6_v32_v32_b_u[_p]
name
Spec syntax   vbextract {Oop, b [,u]} vx[0], #width6, vy[Ye], vz[0], ?vprX

Return type   vec_t

1    OOP             uint8     1..8             Number of atomic operations
              2    IN1_V32         vec_t                      Input vector operand
              3    IN2_WIDTH6 int16          0..63            6 bit unsigned immediate
Operands      4    IN3_V32         vec_t                      Input vector operand

              5    IN3_OFST        uint8     0,2,4,6          Offset for the first DW used from operand
                                                              4

              6    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbextract_v32_width6_v32_v32_b_u_p (8, vIn, 2, vIn2, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for
                vbextract_v32_width6_v32_v32_b_u_p version.


Main table → Bit Manipulation → Bit Extract → Vector Bit Extract
