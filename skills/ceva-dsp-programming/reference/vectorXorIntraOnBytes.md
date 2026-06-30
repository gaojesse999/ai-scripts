# Logic → Xor Intra-Vector → Vector XOR Intra on Bytes

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Logic → Xor Intra-Vector → Vector XOR Intra on Bytes

Vector XOR Intra on Bytes

Vector XOR Intra on Bytes

Performs intra-vector XOR between sources that are located in the same vector. Each source is
8-bit wide. The destination is 8-bit.
Available Switches
None
Intrinsic Names
vxorintb_v32_v32_v32
vxorintb_v32_v32
Instruction details in the instruction set specification
Intrinsic     vxorintb_v32_v32_v32[_p]
name
Spec syntax   vxorintb {Qop} vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    QOP              uint8     1..4              Number of atomic operations
              2    IN1_V32          vec_t                       Input vector operand

              3    IN1_OFST         uint8     0,4
                                                                Offset for the first DW used from operand
                                                                2

              4    IN2_V32          vec_t                       Input vector operand
Operands
              5    IN2_OFST         uint8     0,4
                                                                Offset for the first DW used from operand
                                                                4

                                                                Offset for the first DW used from the
              6    OUT_OFST         uint8     0,4
                                                                result operand
              7    IN_VPR           vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vxorintb_v32_v32_v32_p (4, vIn, 0, vIn2, 0, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vxorintb_v32_v32_v32_p version.


Main table → Logic → Xor Intra-Vector → Vector XOR Intra on Bytes
Intrinsic     vxorintb_v32_v32[_p]
name
Spec syntax   vxorintb {Qop} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP             uint8      1..4             Number of atomic operations
              2    IN1_V32         vec_t                       Input vector operand

              3    IN1_OFST        uint8      0,4
                                                               Offset for the first DW used from operand
Operands                                                       2

                                                               Offset for the first DW used from the
              4    OUT_OFST        uint8      0,4

result operand
              5    IN_VPR          vprex_t                     Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vxorintb_v32_v32_p (4, vIn, 0, 0, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vxorintb_v32_v32_p version.


Main table → Logic → Xor Intra-Vector → Vector XOR Intra on Bytes
