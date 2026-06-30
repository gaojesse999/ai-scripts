# Floating Point → Float Multiplication → Vector Floating Point Multiply and

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Floating Point → Float Multiplication → Vector Floating Point Multiply and
Accumulate

Vector Floating Point Multiply and Accumulate

Vector Floating Point Multiply and Accumulate
Performs multiply-accumulate between two 32-bit single precision floating-point sources into a
destination. The sources and the destination are either 32-bit or 40-bit wide determined by the
vector register type. This is a non-native instruction and is implemented as software sequence.
Available Switches
None
Intrinsic Names
vflpmac
Instruction details in the instruction set specification
Intrinsic     vflpmac[_p]
name
Spec syntax   vflpmac vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t              Input vector operand
              2    IN2_V32         vec_t              Input vector operand
Operands
              3    IN3_V32         vec_t              Input vector operand
              4    IN_VPR          vprex_t            Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vflpmac_p(vIn, vIn2, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vflpmac_p version.
Comments           vflpmac is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float Multiplication → Vector Floating Point Multiply and
Accumulate

Main table → Floating Point → Float Multiplication → Vector Floating Point Multiply and
Substract

Vector Floating Point Multiply and Substract

Vector Floating Point Multiply and Substract
Performs multiply-subtract between two 32-bit single precision floating-point sources into a
destination. The sources and the destination are either 32-bit or 40-bit wide determined by the
vector register type. This is a non-native instruction and is implemented as software sequence.
Available Switches
None
Intrinsic Names
vflpmsu
Instruction details in the instruction set specification
Intrinsic     vflpmsu[_p]
name
Spec syntax   vflpmsu vx[0], vy[0], vz[0], ?vprX

Return type   vec_t

              1    IN1_V32         vec_t              Input vector operand
              2    IN2_V32         vec_t              Input vector operand
Operands

3    IN3_V32         vec_t              Input vector operand
              4    IN_VPR          vprex_t            Vector predicate operand
              vec_t vIn;
              vec_t vIn2;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vflpmsu_p(vIn, vIn2, vRes, vecPred);

              1.   IN_VPR last operand is relevant only for vflpmsu_p version.
Comments           vflpmsu is a macro which expands into a sequence of several Vec-C
              2.
                   intrinsics. For macro definition, click the "Spec Syntax" link above.


Main table → Floating Point → Float Multiplication → Vector Floating Point Multiply and
Substract
