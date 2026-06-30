# Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes

Vector Bit Unpack into Bytes

Vector Bit Unpack into Bytes
Performs unpacking of bits into byte destinations.
Available Switches
       Number of atomic operations. An atomic operation is defined by as four unpack
Oop
       operations. 1op ≤ Oop ≤ 8op.
kbit Number of bits which are unpacked from vx[X] registers. 1 ≤ kbit ≤ 7.
se     When used, the destination is sign-extended. The default is zero-extended.
Intrinsic Names
vbunpackb_v32_v32_1bit_2p
vbunpackb_v32_v32_1bit_se_2p
vbunpackb_v32_v32_2bit_2p
vbunpackb_v32_v32_2bit_se_2p
vbunpackb_v32_v32_3bit_2p
vbunpackb_v32_v32_3bit_se_2p

vbunpackb_v32_v32_4bit_2p
vbunpackb_v32_v32_4bit_se_2p
vbunpackb_v32_v32_5bit_2p
vbunpackb_v32_v32_5bit_se_2p
vbunpackb_v32_v32_6bit_2p
vbunpackb_v32_v32_6bit_se_2p
vbunpackb_v32_v32_7bit_2p
vbunpackb_v32_v32_7bit_se_2p
vbunpackb_v32_v32_2p
vbunpackb_v32_v32_se_2p
Instruction details in the instruction set specification
Intrinsic     vbunpackb_v32_v32_1bit_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_1bit_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_1bit_se_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_1bit_se_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_2bit_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_2bit_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_2bit_se_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations

Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_2bit_se_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_3bit_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_3bit_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_3bit_se_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_3bit_se_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_4bit_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_4bit_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_4bit_se_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_4bit_se_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_5bit_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_5bit_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_5bit_se_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_5bit_se_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_6bit_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t
              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_6bit_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_6bit_se_p_3p
name

Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_6bit_se_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_7bit_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_7bit_p_3p (8, vIn, vecPred);

Comments

Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_7bit_se_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_7bit_se_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands      2    IN1_V32        vec_t                     Input vector operand
              3    IN_VPR         vprex_t                   Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vbunpackb_v32_v32_p_3p (8, vIn, vecPred);

Comments

Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
Intrinsic     vbunpackb_v32_v32_se_p_3p
name
Spec syntax   vbunpackb {Oop [,kbit][,se]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    OOP            uint8     1..8            Number of atomic operations
Operands
              2    IN1_V32        vec_t                     Input vector operand
            3    IN_VPR         vprex_t                   Vector predicate operand
            vec_t vIn;
            vec_t vRes;
C example   vprex_t vecPred;
            ...
            vRes = vbunpackb_v32_v32_se_p_3p (8, vIn, vecPred);

Comments


Main table → Bit Manipulation → Bit Unpack → Vector Bit Unpack into Bytes
