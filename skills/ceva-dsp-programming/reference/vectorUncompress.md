# Bit Manipulation → Uncompress → Vector Uncompress

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Bit Manipulation → Uncompress → Vector Uncompress

Vector Uncompress

Vector Uncompress
Uncompresses a source of the range 9 to15-bits wide depending on the instruction switch into a
destination of either 16-bit or 20-bit wide destination determined by the register type.
Available Switches
isize       Input size ranges from isize bits 9 ≤ isize ≤ 15
u           When used, the destination is zero-extended. The default is sign-extended.
Intrinsic Names
vuncompress_v32_v32_isize
vuncompress_v32_v32_isize_u
Instruction details in the instruction set specification
Intrinsic     vuncompress_v32_v32_isize[_p]
name
Spec syntax   vuncompress {isize [,u]} vx[0], vz[0], ?vprX

Return type   vec_t

              1    ISIZE          uint8     9..15            Width of the input to be uncompressed
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vuncompress_v32_v32_isize_p (15, vIn, vecPred);

                   IN_VPR last operand is relevant only for vuncompress_v32_v32_isize_p
Comments      1.
                   version.


Main table → Bit Manipulation → Uncompress → Vector Uncompress
Intrinsic     vuncompress_v32_v32_isize_u[_p]
name
Spec syntax   vuncompress {isize [,u]} vx[0], vz[0], ?vprX

Return type   vec_t

1    ISIZE          uint8     9..15            Width of the input to be uncompressed
Operands      2    IN1_V32        vec_t                      Input vector operand
              3    IN_VPR         vprex_t                    Vector predicate operand
              vec_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vuncompress_v32_v32_isize_u_p (15, vIn, vecPred);

                   IN_VPR last operand is relevant only for vuncompress_v32_v32_isize_u_p
Comments      1.
                   version.


Main table → Bit Manipulation → Uncompress → Vector Uncompress
