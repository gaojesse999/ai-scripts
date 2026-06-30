# Bit Manipulation → Compress → Vector Compress

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Compress → Vector Compress

Vector Compress

Vector Compress

Compresses a source of 16-bits into an output ranging from 9 to 15-bits wide depending on the
instruction switch.
Available Switches
isize          Input size ranges from isize bits 9 ≤ isize ≤ 15
Intrinsic Names
vcompress_v32_v32_isize
Instruction details in the instruction set specification
Intrinsic     vcompress_v32_v32_isize[_p]
name
Spec syntax   vcompress {isize} vx[0], vz[0], ?vprX

Return type   vec_t

              1    ISIZE           uint8     9..15            Width of the output to be compressed
Operands      2    IN1_V32         vec_t                      Input vector operand
              3    IN_VPR          vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vcompress_v32_v32_isize_p (15, vIn, vecPred);

                   IN_VPR last operand is relevant only for vcompress_v32_v32_isize_p
Comments      1.
                   version.


Main table → Bit Manipulation → Compress → Vector Compress
