# Special Algorithms → Hermitian Matrix Determinant → Vector Hermitian

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Special Algorithms → Hermitian Matrix Determinant → Vector Hermitian
Matrix Determinant

Vector Hermitian Matrix Determinant

Vector Hermitian Matrix Determinant
Performs 2x2 Hermitian matrix determinant calculation. Each source is 16-bit wide. The
destination is 40-bit wide.
Available Switches
       Number of atomic operations. An atomic operation is defined as a single Hermitian matrix
Qop
       determinant operation. 1op ≤ Qop ≤ 4op
Intrinsic Names
vhmdet_v32_v32
Instruction details in the instruction set specification
Intrinsic     vhmdet_v32_v32[_p]
name
Spec syntax   vhmdet {Qop} vx[0], vz[0], ?vprX

Return type   vec_t

              1    QOP            uint8     1..4           Number of atomic operations
Operands      2    IN1_V32        vec_t                    Input vector operand
              3    IN_VPR         vprex_t                  Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vhmdet_v32_v32_p (4, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vhmdet_v32_v32_p version.


Main table → Special Algorithms → Hermitian Matrix Determinant → Vector Hermitian
Matrix Determinant
