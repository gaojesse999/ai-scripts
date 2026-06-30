# Memory Access → Load → Load unsigned W unrounded

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Memory Access → Load → Load unsigned W unrounded

Load unsigned W unrounded

Load unsigned W unrounded
Load unsigned 16 bit word without rounding. Each result which is written is zero-extended
instead of sign-extended.
Available Switches
2w         Two word loads
4w         Four word loads
dup        The data brought from the memory is duplicated
ew         Number of word loads. ew can be 2w, 4w, 6w or 8w
           Rounding constant. When used, each voz[Z]h which is written, the low part is written
r
           with 0x8000
           When row stride mechanism enabled - the row stride values are taken from ROWSTR0
rowstr
           or ROWSTR1 located under mod4 mode register.
strX       Selects the STR, PMSTR set within mod1 register and ROWSTR at mod4 register.
           When used, each voz[Z] which is written is zero-extended instead of sign-extended (the
u
           default is sign-extension)
           When 'unpk' switch is used 16w words of data are brought from the memory and
unpk
           unpacked into the two vector destinations - each vector is unpacked from 8w.
vuX        Determines the destination VCU of the instruction. X is replaced by 0 or 1.
Intrinsic Names
vldw_v40_v40_8w_unpk_u
vldw_v40_v40_8w_unpk_u_rowstr
vldw_v40_v40_clone_8w_unpk_u
vldw_v40_v40_clone_8w_unpk_u_rowstr
vldw_v40_vuX_u
vldw_v40_clone_u
vldw_v40_clone_u_rowstr
vldw_v40_u
vldw_v40_u_rowstr
vldw_v40_2w_dup_u
vldw_v40_2w_dup_u_rowstr
vldw_v40_4w_dup_u
vldw_v40_4w_dup_u_rowstr
vldw_v40_clone_2w_dup_u
vldw_v40_clone_2w_dup_u_rowstr
vldw_v40_clone_4w_dup_u
vldw_v40_clone_4w_dup_u_rowstr
Instruction details in the instruction set specification
Available addressing modes
Intrinsic Names:
vldw_direct_v40_v40_8w_unpk_u
vldw_indexed_imm_v40_v40_8w_unpk_u
vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u
vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u
vldw_indexed_rI_v40_v40_8w_unpk_u
vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u
vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u
vldw_indexed_rIp_v40_v40_8w_unpk_u
vldw_pm_imm_v40_v40_8w_unpk_u
vldw_pm_ptr_v40_v40_8w_unpk_u
vldw_v40_v40_8w_unpk_u

Intrinsic     vldw_direct_v40_v40_8w_unpk_u
name
Spec syntax   vldw {8w, unpk [,u][,strX]} [#address], voz1[0]l, voz2[0]l [,?prSC]

Return type   vec40_t
                                               32
              1    IN1_ADDR       int32     0..2 -1         32 bit address
              2    RES2_V40       vec40_t                   Output vector result operand
Operands
                                                            Word part which is used for the result
              3    OUT_PART       uint8     LOW,HIGH
                                                            operand
              vec40_t vRes1;
              vec40_t vRes2;
C example     ...
              vRes1 = vldw_direct_v40_v40_8w_unpk_u (2, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_imm_v40_v40_8w_unpk_u
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+#imm16_6), voz1[0]l, voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                       Pointer register (gB)
                                                            16 bit immediate post modification in
              2    IN2_IMM16_6    int16     -32768..32767
                                                            bytes
Operands
              3    RES2_V40       vec40_t                   Output vector result operand
                                                            Word part which is used for the result
              4    OUT_PART       uint8     LOW,HIGH
                                                            operand
              void* ptrBase;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_imm_v40_v40_8w_unpk_u (ptrBase, 2, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
                                               31   31       32 bit immediate post modification in
Operands      3    IN3_PM_IMM       int32     -2 ..2 -1
                                                             bytes
              4    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              5    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u (ptrBase, ptrModify, 2, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands      3    IN3_PM_PTR       void*                    Pointer register (rN)
              4    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              5    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u (ptrBase, ptrModify, ptr, vRes2, LOW);

Comments      1.   This intrinsic returns two results. The first result variable should be placed to
                   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_v40_v40_8w_unpk_u
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              4    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_v40_v40_8w_unpk_u (ptrBase, ptrModify, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8     LOW,HIGH       Word part which is used for operand 2
Operands                                       31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32     -2 ..2 -1
                                                             bytes
              5    RES2_V40         vec40_t                  Output vector result operand

              6

Word part which is used for the result
                   OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u (ptrBase, ptrModify, LOW, 2, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

              2
                                                             Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8     LOW,HIGH       Word part which is used for operand 2
Operands
              4    IN3_PM_PTR       void*                    Pointer register (rN)
              5    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              6    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u (ptrBase, ptrModify, LOW, ptr, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_v40_v40_8w_unpk_u
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands

2    IN2_rI_OFFSET void *                      Pointer (rI) specifying the offset from the
                                                            base pointer
              3    IN2_PART        uint8      LOW,HIGH      Word part which is used for operand 2
              4    RES2_V40        vec40_t                  Output vector result operand
                                                            Word part which is used for the result
              5    OUT_PART        uint8      LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_v40_v40_8w_unpk_u (ptrBase, ptrModify, LOW, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_imm_v40_v40_8w_unpk_u
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (pN)+#imm32_6, voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                    Pointer register (rN)
                                              31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32         -2 ..2 -1
                                                            bytes
Operands
              3    RES2_V40       vec40_t                   Output vector result operand

              4
                                                            Word part which is used for the result
                   OUT_PART       uint8      LOW,HIGH
                                                            operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_pm_imm_v40_v40_8w_unpk_u (ptr, 2, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_ptr_v40_v40_8w_unpk_u
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (pN)[+pm_x], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

1    IN1_PTR        void *                   Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
Operands      3    RES2_V40       vec40_t                  Output vector result operand
                                                           Word part which is used for the result
              4    OUT_PART       uint8     LOW,HIGH
                                                           operand
              vec40_t ptr;
              void* vRes1;
C example     vec40_t vRes2;
              ...
              vRes2 = vldw_pm_ptr_v40_v40_8w_unpk_u (ptr, vRes1, ptr, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_v40_v40_8w_unpk_u
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (pN)[+pm_x], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
              2    RES2_V40       vec40_t                  Output vector result operand
Operands
                                                           Word part which is used for the result
              3    OUT_PART       uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_v40_v40_8w_unpk_u (ptr, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_v40_8w_unpk_u_rowstr
vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u_rowstr
vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u_rowstr
vldw_indexed_rI_v40_v40_8w_unpk_u_rowstr
vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u_rowstr
vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u_rowstr
vldw_indexed_rIp_v40_v40_8w_unpk_u_rowstr
vldw_pm_imm_v40_v40_8w_unpk_u_rowstr
vldw_pm_ptr_v40_v40_8w_unpk_u_rowstr
vldw_v40_v40_8w_unpk_u_rowstr
Intrinsic     vldw_indexed_imm_v40_v40_8w_unpk_u_rowstr
name

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+#imm16_6), voz1[0]l, voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                         Pointer register (gB)
                                                              16 bit immediate post modification in
              2    IN2_IMM16_6     int16      -32768..32767
                                                              bytes
Operands
              3    RES2_V40        vec40_t                    Output vector result operand
                                                              Word part which is used for the result
              4    OUT_PART        uint8      LOW,HIGH
                                                              operand
              void* ptrBase;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_imm_v40_v40_8w_unpk_u_rowstr (ptrBase, 2, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
                                                31   31       32 bit immediate post modification in
Operands      3    IN3_PM_IMM       int32     -2 ..2 -1
                                                              bytes
              4    RES2_V40         vec40_t                   Output vector result operand
                                                              Word part which is used for the result
              5    OUT_PART         uint8     LOW,HIGH
                                                              operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_imm_v40_v40_8w_unpk_u_rowstr (ptrBase, ptrModify, 2, vRes2, LOW);

This intrinsic returns two results. The first result variable should be placed to
Comments      1.
                   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands      3    IN3_PM_PTR       void*                    Pointer register (rN)
              4    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              5    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_ptr_v40_v40_8w_unpk_u_rowstr (ptrBase, ptrModify, ptr, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_v40_v40_8w_unpk_u_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

              2
                                                             Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              4    OUT_PART         uint8     LOW,HIGH
                                                             operand

void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_v40_v40_8w_unpk_u_rowstr (ptrBase, ptrModify, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8     LOW,HIGH       Word part which is used for operand 2
Operands                                       31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32     -2 ..2 -1
                                                             bytes
              5    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              6    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_imm_v40_v40_8w_unpk_u_rowstr (ptrBase, ptrModify, LOW, 2, vRes2,
              LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the

2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8     LOW,HIGH       Word part which is used for operand 2
              4    IN3_PM_PTR       void*                    Pointer register (rN)
              5    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              6    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_ptr_v40_v40_8w_unpk_u_rowstr (ptrBase, ptrModify, LOW, ptr, vRes2,
              LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_v40_v40_8w_unpk_u_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands      3    IN2_PART         uint8     LOW,HIGH       Word part which is used for operand 2
              4    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              5    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_v40_v40_8w_unpk_u_rowstr (ptrBase, ptrModify, LOW, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as

an additional parameter (RES2_V40).



Intrinsic     vldw_pm_imm_v40_v40_8w_unpk_u_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (pN)+#imm32_6, voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                    Pointer register (rN)
                                             31   31        32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
                                                            bytes
Operands
              3    RES2_V40       vec40_t                   Output vector result operand
                                                            Word part which is used for the result
              4    OUT_PART       uint8     LOW,HIGH
                                                            operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_pm_imm_v40_v40_8w_unpk_u_rowstr (ptr, 2, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_ptr_v40_v40_8w_unpk_u_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (pN)[+pm_x], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
Operands      3    RES2_V40       vec40_t                  Output vector result operand
                                                           Word part which is used for the result
              4    OUT_PART       uint8     LOW,HIGH
                                                           operand
              vec40_t ptr;
              void* vRes1;
C example     vec40_t vRes2;
              ...
              vRes2 = vldw_pm_ptr_v40_v40_8w_unpk_u_rowstr (ptr, vRes1, ptr, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_v40_v40_8w_unpk_u_rowstr
name
Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (pN)[+pm_x], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
              2    RES2_V40       vec40_t                  Output vector result operand
Operands
                                                           Word part which is used for the result
              3    OUT_PART       uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_v40_v40_8w_unpk_u_rowstr (ptr, vRes2, LOW);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_v40_clone_8w_unpk_u
vldw_indexed_imm_v40_v40_clone_8w_unpk_u
vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u
vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u
vldw_indexed_rI_v40_v40_clone_8w_unpk_u
vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u
vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u
vldw_indexed_rIp_v40_v40_clone_8w_unpk_u
vldw_pm_imm_v40_v40_clone_8w_unpk_u
vldw_pm_ptr_v40_v40_clone_8w_unpk_u
vldw_v40_v40_clone_8w_unpk_u
Intrinsic     vldw_direct_v40_v40_clone_8w_unpk_u
name          vldw_direct_v40_v40_str1_8w_unpk_u

Spec syntax   vldw {8w, unpk [,u][,strX]} [#address], voz1[0]l, voz2[0]l [,?prSC]

Return type   vec40_t
                                               32
              1    IN1_ADDR       int32     0..2 -1         32 bit address
              2    RES2_V40       vec40_t                   Output vector result operand
Operands
                                                            Word part which is used for the result
              3    OUT_PART       uint8     LOW,HIGH
                                                            operand
              vec40_t vRes1;
              vec40_t vRes2;
C example     ...
              vRes1 = vldw_direct_v40_v40_clone_8w_unpk_u (2, vRes2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to

2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_imm_v40_v40_clone_8w_unpk_u
name          vldw_indexed_imm_v40_v40_str1_8w_unpk_u

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+#imm16_6), voz1[0]l, voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                       Pointer register (gB)
                                                            16 bit immediate post modification in
              2    IN2_IMM16_6    int16     -32768..32767
                                                            bytes
Operands
              3    RES2_V40       vec40_t                   Output vector result operand
                                                            Word part which is used for the result
              4    OUT_PART       uint8     LOW,HIGH
                                                            operand
              void* ptrBase;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_imm_v40_v40_clone_8w_unpk_u (ptrBase, 2, vRes2, LOW);

              1.
                   The same data will be loaded to all vector units (Unless str1 is configured
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).
Intrinsic     vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u
name          vldw_indexed_rI_pm_imm_v40_v40_str1_8w_unpk_u

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
                                               31   31       32 bit immediate post modification in
Operands      3    IN3_PM_IMM       int32     -2 ..2 -1
                                                             bytes
              4    RES2_V40         vec40_t                  Output vector result operand

Word part which is used for the result
              5    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u (ptrBase, ptrModify, 2, vRes2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u
name          vldw_indexed_rI_pm_ptr_v40_v40_str1_8w_unpk_u

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands      3    IN3_PM_PTR       void*                    Pointer register (rN)
              4    RES2_V40         vec40_t                  Output vector result operand

              5    OUT_PART         uint8
                                                             Word part which is used for the result
                                              LOW,HIGH
                                                             operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u (ptrBase, ptrModify, ptr, vRes2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).

Intrinsic     vldw_indexed_rI_v40_v40_clone_8w_unpk_u
name          vldw_indexed_rI_v40_v40_str1_8w_unpk_u

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              4    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_v40_v40_clone_8w_unpk_u (ptrBase, ptrModify, vRes2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u
name          vldw_indexed_rIp_pm_imm_v40_v40_str1_8w_unpk_u

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t
              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8     LOW,HIGH       Word part which is used for operand 2
Operands                                       31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32     -2 ..2 -1
                                                             bytes
              5    RES2_V40         vec40_t                  Output vector result operand

Word part which is used for the result
              6    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u (ptrBase, ptrModify, LOW, 2, vRes2,
              LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u
name          vldw_indexed_rIp_pm_ptr_v40_v40_str1_8w_unpk_u

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

              2
                                                             Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8     LOW,HIGH       Word part which is used for operand 2
Operands
              4    IN3_PM_PTR       void*                    Pointer register (rN)
              5    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              6    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptr;
              void* ptrBase;
C example     void* ptrModify;
              vec40_t vRes1;
              vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u (ptrBase, ptrModify, LOW, ptr, vRes2,
              LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to

2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_v40_v40_clone_8w_unpk_u
name          vldw_indexed_rIp_v40_v40_str1_8w_unpk_u

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands      3    IN2_PART         uint8     LOW,HIGH       Word part which is used for operand 2
              4    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              5    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_v40_v40_clone_8w_unpk_u (ptrBase, ptrModify, LOW, vRes2, LOW);

              1.
                   The same data will be loaded to all vector units (Unless str1 is configured
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_imm_v40_v40_clone_8w_unpk_u
name          vldw_pm_imm_v40_v40_str1_8w_unpk_u

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (pN)+#imm32_6, voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

Operands      1    IN1_PTR        void *                    Pointer register (rN)
                                             31   31        32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
                                                            bytes
              3    RES2_V40       vec40_t                   Output vector result operand

              4
                                                            Word part which is used for the result

OUT_PART       uint8     LOW,HIGH
                                                            operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_pm_imm_v40_v40_clone_8w_unpk_u (ptr, 2, vRes2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_ptr_v40_v40_clone_8w_unpk_u
name          vldw_pm_ptr_v40_v40_str1_8w_unpk_u

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (pN)[+pm_x], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
Operands      3    RES2_V40       vec40_t                  Output vector result operand
                                                           Word part which is used for the result
              4    OUT_PART       uint8     LOW,HIGH
                                                           operand
              vec40_t ptr;
              void* vRes1;
C example     vec40_t vRes2;
              ...
              vRes2 = vldw_pm_ptr_v40_v40_clone_8w_unpk_u (ptr, vRes1, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_v40_v40_clone_8w_unpk_u
name          vldw_v40_v40_str1_8w_unpk_u
Spec syntax    vldw {8w, unpk [,u][,strX][,rowstr]} (pN)[+pm_x], voz1[0]l ,voz2[0]l [,?prSC]

Return type    vec40_t

               1    IN1_PTR        void *                   Pointer register (rN)
               2    RES2_V40       vec40_t                  Output vector result operand
Operands
                                                            Word part which is used for the result
               3    OUT_PART       uint8     LOW,HIGH

operand
               void* ptr;
               vec40_t vRes1;
C example      vec40_t vRes2;
               ...
               vRes1 = vldw_v40_v40_clone_8w_unpk_u (ptr, vRes2, LOW);

                    The same data will be loaded to all vector units (Unless str1 is configured
               1.
                    otherwise).
Comments            This intrinsic returns two results. The first result variable should be placed to
               2.   the left of the = sign (lvalue). The second result variable should be passed as
                    an additional parameter (RES2_V40).


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_v40_clone_8w_unpk_u_rowstr
vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u_rowstr
vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u_rowstr
vldw_indexed_rI_v40_v40_clone_8w_unpk_u_rowstr
vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u_rowstr
vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u_rowstr
vldw_indexed_rIp_v40_v40_clone_8w_unpk_u_rowstr
vldw_pm_imm_v40_v40_clone_8w_unpk_u_rowstr
vldw_pm_ptr_v40_v40_clone_8w_unpk_u_rowstr
vldw_v40_v40_clone_8w_unpk_u_rowstr
Intrinsic     vldw_indexed_imm_v40_v40_clone_8w_unpk_u_rowstr
name          vldw_indexed_imm_v40_v40_str1_8w_unpk_u_rowstr

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+#imm16_6), voz1[0]l, voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                         Pointer register (gB)
                                                              16 bit immediate post modification in
              2    IN2_IMM16_6     int16      -32768..32767
                                                              bytes
Operands
              3    RES2_V40        vec40_t                    Output vector result operand
                                                              Word part which is used for the result
              4    OUT_PART        uint8      LOW,HIGH
                                                              operand
              void* ptrBase;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_imm_v40_v40_clone_8w_unpk_u_rowstr (ptrBase, 2, vRes2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u_rowstr
name          vldw_indexed_rI_pm_imm_v40_v40_str1_8w_unpk_u_rowstr

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
                                                31   31       32 bit immediate post modification in
Operands      3    IN3_PM_IMM       int32     -2 ..2 -1
                                                              bytes
              4    RES2_V40         vec40_t                   Output vector result operand

              5
                                                              Word part which is used for the result
                   OUT_PART         uint8     LOW,HIGH
                                                              operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_imm_v40_v40_clone_8w_unpk_u_rowstr (ptrBase, ptrModify, 2, vRes2,
              LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u_rowstr
name          vldw_indexed_rI_pm_ptr_v40_v40_str1_8w_unpk_u_rowstr

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the

2    IN2_rI_OFFSET void *
                                                             base pointer
Operands      3    IN3_PM_PTR       void*                    Pointer register (rN)
              4    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              5    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_pm_ptr_v40_v40_clone_8w_unpk_u_rowstr (ptrBase, ptrModify, ptr, vRes2,
              LOW);

              1.
                   The same data will be loaded to all vector units (Unless str1 is configured
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rI_v40_v40_clone_8w_unpk_u_rowstr
name          vldw_indexed_rI_v40_v40_str1_8w_unpk_u_rowstr

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rI)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

Operands      1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    RES2_V40         vec40_t                  Output vector result operand

              4
                                                             Word part which is used for the result
                   OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rI_v40_v40_clone_8w_unpk_u_rowstr (ptrBase, ptrModify, vRes2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).

Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u_rowstr
name          vldw_indexed_rIp_pm_imm_v40_v40_str1_8w_unpk_u_rowstr

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8     LOW,HIGH       Word part which is used for operand 2
Operands                                       31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32     -2 ..2 -1
                                                             bytes
              5    RES2_V40         vec40_t                  Output vector result operand
                                                             Word part which is used for the result
              6    OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_imm_v40_v40_clone_8w_unpk_u_rowstr (ptrBase, ptrModify, LOW, 2,
              vRes2, LOW);

              1.
                   The same data will be loaded to all vector units (Unless str1 is configured
Comments           otherwise).
              2.   This intrinsic returns two results. The first result variable should be placed to
                   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u_rowstr
name          vldw_indexed_rIp_pm_ptr_v40_v40_str1_8w_unpk_u_rowstr

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8     LOW,HIGH       Word part which is used for operand 2
Operands
              4    IN3_PM_PTR       void*                    Pointer register (rN)
              5    RES2_V40         vec40_t                  Output vector result operand

              6
                                                             Word part which is used for the result
                   OUT_PART         uint8     LOW,HIGH
                                                             operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_indexed_rIp_pm_ptr_v40_v40_clone_8w_unpk_u_rowstr (ptrBase, ptrModify, LOW, ptr,
              vRes2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_indexed_rIp_v40_v40_clone_8w_unpk_u_rowstr
name          vldw_indexed_rIp_v40_v40_str1_8w_unpk_u_rowstr

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8     LOW,HIGH       Word part which is used for operand 2
              4    RES2_V40        vec40_t                  Output vector result operand
                                                            Word part which is used for the result
              5    OUT_PART        uint8      LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...

vRes1 = vldw_indexed_rIp_v40_v40_clone_8w_unpk_u_rowstr (ptrBase, ptrModify, LOW, vRes2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_imm_v40_v40_clone_8w_unpk_u_rowstr
name          vldw_pm_imm_v40_v40_str1_8w_unpk_u_rowstr

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (pN)+#imm32_6, voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                    Pointer register (rN)
                                              31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32         -2 ..2 -1
                                                            bytes
Operands
              3    RES2_V40       vec40_t                   Output vector result operand
                                                            Word part which is used for the result
              4    OUT_PART       uint8      LOW,HIGH
                                                            operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_pm_imm_v40_v40_clone_8w_unpk_u_rowstr (ptr, 2, vRes2, LOW);

              1.
                   The same data will be loaded to all vector units (Unless str1 is configured
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_pm_ptr_v40_v40_clone_8w_unpk_u_rowstr
name          vldw_pm_ptr_v40_v40_str1_8w_unpk_u_rowstr

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (pN)[+pm_x], voz1[0]l ,voz2[0]l [,?prSC]
Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
Operands      3    RES2_V40       vec40_t                  Output vector result operand

Word part which is used for the result
              4    OUT_PART       uint8     LOW,HIGH
                                                           operand
              vec40_t ptr;
              void* vRes1;
C example     vec40_t vRes2;
              ...
              vRes2 = vldw_pm_ptr_v40_v40_clone_8w_unpk_u_rowstr (ptr, vRes1, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).



Intrinsic     vldw_v40_v40_clone_8w_unpk_u_rowstr
name          vldw_v40_v40_str1_8w_unpk_u_rowstr

Spec syntax   vldw {8w, unpk [,u][,strX][,rowstr]} (pN)[+pm_x], voz1[0]l ,voz2[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
              2    RES2_V40       vec40_t                  Output vector result operand
Operands
                                                           Word part which is used for the result
              3    OUT_PART       uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes1;
C example     vec40_t vRes2;
              ...
              vRes1 = vldw_v40_v40_clone_8w_unpk_u_rowstr (ptr, vRes2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_V40).


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_pm_imm_v40_vuX_u
vldw_pm_ptr_v40_vuX_u
vldw_v40_vuX_u
Intrinsic     vldw_pm_imm_v40_vuX_u
name
Spec syntax   vldw {ew, vuX [,u]} (pN)[+pm_x], voz[0]l [,?prSC]

Return        vec40_t
type
                                                             Determines the element size and number
                                 EW_options
              1   EW

enum                        of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
              2   VUX            uint8         0..3          Determines the destination VCU
Operands      3   IN1_PTR        void *                      Pointer register (rN)
                                                 31   31     32 bit immediate post modification in
              4   IN2_PM_IMM int32             -2 ..2 -1
                                                             bytes
                                                             Word part which is used for the result
              5   OUT_PART       uint8         LOW,HIGH
                                                             operand
              vec40_t 2;
              void* ptr;
C example     ...
              2 = vldw_pm_imm_v40_vuX_u (ew_8w, 1, ptr, vRes, LOW);

Comments



Intrinsic     vldw_pm_ptr_v40_vuX_u
name
Spec          vldw {ew, vuX [,u]} (pN)[+pm_x], voz[0]l [,?prSC]
syntax
Return        vec40_t
type
                                                              Determines the element size and number
                                EW_options
              1   EW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
              2   VUX           uint8          0..3           Determines the destination VCU
Operands      3   IN1_PTR       void *                        Pointer register (rN)
              4   IN2_PM_PTR void*                            Pointer register (rN)
                                                              Word part which is used for the result
              5   OUT_PART      uint8          LOW,HIGH
                                                              operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_vuX_u (ew_8w, 1, ptr, vRes, LOW);
Comments



Intrinsic     vldw_v40_vuX_u
name
Spec syntax   vldw {ew, vuX [,u]} (pN)[+pm_x], voz[0]l [,?prSC]

Return        vec40_t
type
                                                            Determines the element size and number
                                EW_options
              1   EW
                                enum                        of loaded elements (see enum definition

at vec-mem-modes.h)

Operands      2   VUX           uint8         0..3          Determines the destination VCU
              3   IN1_PTR       void *                      Pointer register (rN)
                                                            Word part which is used for the result
              4   OUT_PART      uint8         LOW,HIGH
                                                            operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_vuX_u (ew_8w, 1, ptr, LOW);

Comments


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_clone_u
vldw_indexed_imm_v40_clone_u
vldw_indexed_rI_pm_imm_v40_clone_u
vldw_indexed_rI_pm_ptr_v40_clone_u
vldw_indexed_rI_v40_clone_u
vldw_indexed_rIp_pm_imm_v40_clone_u
vldw_indexed_rIp_pm_ptr_v40_clone_u
vldw_indexed_rIp_v40_clone_u
vldw_pm_imm_v40_clone_u
vldw_pm_ptr_v40_clone_u
vldw_v40_clone_u
Intrinsic     vldw_direct_v40_clone_u
name          vldw_direct_v40_str1_u

Spec syntax   vldw {ew [,u][,strX]} [#address], voz[0]l [,?prSC]

Return        vec40_t
type
                                                                Determines the element size and number
                                 EW_options
              1    EW
                                 enum                           of loaded elements (see enum definition
                                                                at vec-mem-modes.h)
Operands                                          32
              2    IN1_ADDR      int32         0..2 -1          32 bit address
                                                                Word part which is used for the result
              3    OUT_PART      uint8         LOW,HIGH
                                                                operand
              vec40_t vRes;
C example     ...
              vRes = vldw_direct_v40_clone_u (ew_8w, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_imm_v40_clone_u
name          vldw_indexed_imm_v40_str1_u

Spec          vldw {ew [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]
syntax
Return        vec40_t
type
                                                                Determines the element size and number
                                  EW_options
              1    EW

enum                          of loaded elements (see enum definition
                                                                at vec-mem-modes.h)
              2    IN1_gB_BASE void *                           Pointer register (gB)
Operands
                                                -               16 bit immediate post modification in
              3    IN2_IMM16_6    int16
                                                32768..32767    bytes

              4
                                                                Word part which is used for the result
                   OUT_PART       uint8         LOW,HIGH
                                                                operand
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_clone_u (ew_8w, ptrBase, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).
Intrinsic   vldw_indexed_rI_pm_imm_v40_clone_u
name        vldw_indexed_rI_pm_imm_v40_str1_u

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
Operands    3    IN2_rI_OFFSET void *
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            4    IN3_PM_IMM      int32         -2 ..2 -1
                                                              bytes
                                                              Word part which is used for the result
            5    OUT_PART        uint8         LOW,HIGH
                                                              operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_imm_v40_clone_u (ew_8w, ptrBase, ptrModify, 2, LOW);

The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rI_pm_ptr_v40_clone_u
name        vldw_indexed_rI_pm_ptr_v40_str1_u

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                       Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                              base pointer
            4    IN3_PM_PTR      void*                        Pointer register (rN)
            5    OUT_PART        uint8         LOW,HIGH       Word part which is used for the result
                                                              operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_ptr_v40_clone_u (ew_8w, ptrBase, ptrModify, ptr, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rI_v40_clone_u
name        vldw_indexed_rI_v40_str1_u

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                       Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                              base pointer

Word part which is used for the result
            4    OUT_PART        uint8         LOW,HIGH
                                                              operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_v40_clone_u (ew_8w, ptrBase, ptrModify, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rIp_pm_imm_v40_clone_u
name        vldw_indexed_rIp_pm_imm_v40_str1_u

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                 EW_options
Operands    1    EW
                                 enum                         Determines the element size and number
                                                             of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                      Pointer register (gB)

            3
                                                             Pointer (rI) specifying the offset from the
                 IN2_rI_OFFSET void *
                                                             base pointer
            4    IN2_PART        uint8         LOW,HIGH      Word part which is used for operand 3
                                                 31   31     32 bit immediate post modification in
            5    IN3_PM_IMM      int32         -2 ..2 -1
                                                             bytes
                                                             Word part which is used for the result
            6    OUT_PART        uint8         LOW,HIGH
                                                             operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_imm_v40_clone_u (ew_8w, ptrBase, ptrModify, LOW, 2, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rIp_pm_ptr_v40_clone_u
name        vldw_indexed_rIp_pm_ptr_v40_str1_u

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type

Determines the element size and number
                                 EW_options
            1    EW
                                 enum                        of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                      Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands    3    IN2_rI_OFFSET void *
                                                             base pointer
            4    IN2_PART        uint8         LOW,HIGH      Word part which is used for operand 3
            5    IN3_PM_PTR      void*                       Pointer register (rN)

            6
                                                             Word part which is used for the result
                 OUT_PART        uint8         LOW,HIGH
                                                             operand
            void* ptr;
            void* ptrBase;
C example   void* ptrModify;
            vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_ptr_v40_clone_u (ew_8w, ptrBase, ptrModify, LOW, ptr, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rIp_v40_clone_u
name        vldw_indexed_rIp_v40_str1_u

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                 EW_options
            1    EW
                                 enum                        of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                      Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                             base pointer
            4    IN2_PART        uint8         LOW,HIGH      Word part which is used for operand 3
                                                             Word part which is used for the result
            5    OUT_PART        uint8         LOW,HIGH

operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_v40_clone_u (ew_8w, ptrBase, ptrModify, LOW, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_pm_imm_v40_clone_u
name        vldw_pm_imm_v40_str1_u

Spec        vldw {ew [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                               EW_options
            1    EW
                               enum                          of loaded elements (see enum definition
Operands                                                     at vec-mem-modes.h)
            2    IN1_PTR       void *                        Pointer register (rN)
                                                 31   31      32 bit immediate post modification in
              3    IN2_IMM32_6 int32           -2 ..2 -1
                                                              bytes
                                                              Word part which is used for the result
              4    OUT_PART      uint8         LOW,HIGH
                                                              operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_clone_u (ew_8w, ptr, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_ptr_v40_clone_u
name          vldw_pm_ptr_v40_str1_u

Spec          vldw {ew [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]
syntax
Return        vec40_t
type
                                                              Determines the element size and number
                                 EW_options
              1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)

Operands      2    IN1_PTR       void *                       Pointer register (rN)
              3    IN2_PM_PTR void*                           Pointer register (rN)
                                                              Word part which is used for the result

4    OUT_PART      uint8         LOW,HIGH
                                                              operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_u (ew_8w, ptr, vRes, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_v40_clone_u
name          vldw_v40_str1_u

Spec syntax   vldw {ew [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return        vec40_t
type
                                EW_options                    Determines the element size and number
Operands      1    EW
                                enum                          of loaded elements (see enum definition
                                                           at vec-mem-modes.h)
              2    IN1_PTR      void *                     Pointer register (rN)

              3
                                                           Word part which is used for the result
                   OUT_PART     uint8         LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_clone_u (ew_8w, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_clone_u_rowstr
vldw_indexed_rI_pm_imm_v40_clone_u_rowstr
vldw_indexed_rI_pm_ptr_v40_clone_u_rowstr
vldw_indexed_rI_v40_clone_u_rowstr
vldw_indexed_rIp_pm_imm_v40_clone_u_rowstr
vldw_indexed_rIp_pm_ptr_v40_clone_u_rowstr
vldw_indexed_rIp_v40_clone_u_rowstr
vldw_pm_imm_v40_clone_u_rowstr
vldw_pm_ptr_v40_clone_u_rowstr
vldw_v40_clone_u_rowstr
Intrinsic   vldw_indexed_imm_v40_clone_u_rowstr
name        vldw_indexed_imm_v40_str1_u_rowstr

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                EW_options
            1    EW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)

2    IN1_gB_BASE void *                           Pointer register (gB)
Operands
                                              -               16 bit immediate post modification in
            3    IN2_IMM16_6    int16
                                              32768..32767    bytes
                                                              Word part which is used for the result
            4    OUT_PART       uint8         LOW,HIGH
                                                              operand
            void* ptrBase;
            vec40_t vRes;
C example   ...
            vRes = vldw_indexed_imm_v40_clone_u_rowstr (ew_8w, ptrBase, 2, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rI_pm_imm_v40_clone_u_rowstr
name        vldw_indexed_rI_pm_imm_v40_str1_u_rowstr

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
Operands    3    IN2_rI_OFFSET void *
                                                              base pointer

            4                                    31   31      32 bit immediate post modification in
                 IN3_PM_IMM      int32         -2 ..2 -1
                                                              bytes
                                                              Word part which is used for the result
            5    OUT_PART        uint8         LOW,HIGH
                                                              operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_imm_v40_clone_u_rowstr (ew_8w, ptrBase, ptrModify, 2, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).

Intrinsic   vldw_indexed_rI_pm_ptr_v40_clone_u_rowstr
name        vldw_indexed_rI_pm_ptr_v40_str1_u_rowstr

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1    EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                       Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
                                                              base pointer
            4    IN3_PM_PTR      void*                        Pointer register (rN)
                                                              Word part which is used for the result
            5    OUT_PART        uint8         LOW,HIGH
                                                              operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_ptr_v40_clone_u_rowstr (ew_8w, ptrBase, ptrModify, ptr, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rI_v40_clone_u_rowstr
name        vldw_indexed_rI_v40_str1_u_rowstr

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                 EW_options
Operands    1    EW
                                 enum                         Determines the element size and number
                                                             of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                      Pointer register (gB)

            3
                                                             Pointer (rI) specifying the offset from the
                 IN2_rI_OFFSET void *
                                                             base pointer

Word part which is used for the result
            4    OUT_PART        uint8         LOW,HIGH
                                                             operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_v40_clone_u_rowstr (ew_8w, ptrBase, ptrModify, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rIp_pm_imm_v40_clone_u_rowstr
name        vldw_indexed_rIp_pm_imm_v40_str1_u_rowstr

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                 EW_options
            1    EW
                                 enum                        of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                      Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
Operands                                                     base pointer
            4    IN2_PART        uint8         LOW,HIGH      Word part which is used for operand 3
                                                 31   31     32 bit immediate post modification in
            5    IN3_PM_IMM      int32         -2 ..2 -1
                                                             bytes
                                                             Word part which is used for the result
            6    OUT_PART        uint8         LOW,HIGH
                                                             operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_imm_v40_clone_u_rowstr (ew_8w, ptrBase, ptrModify, LOW, 2, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).
Intrinsic   vldw_indexed_rIp_pm_ptr_v40_clone_u_rowstr
name        vldw_indexed_rIp_pm_ptr_v40_str1_u_rowstr

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type

Determines the element size and number
                                 EW_options
            1    EW
                                 enum                        of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_gB_BASE     void *                      Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3    IN2_rI_OFFSET void *
Operands                                                     base pointer
            4    IN2_PART        uint8         LOW,HIGH      Word part which is used for operand 3
            5    IN3_PM_PTR      void*                       Pointer register (rN)

            6
                                                             Word part which is used for the result
                 OUT_PART        uint8         LOW,HIGH
                                                             operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_ptr_v40_clone_u_rowstr (ew_8w, ptrBase, ptrModify, LOW, ptr, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_indexed_rIp_v40_clone_u_rowstr
name        vldw_indexed_rIp_v40_str1_u_rowstr

Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                 EW_options
            1    EW
                                 enum                        of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
Operands
            2    IN1_gB_BASE     void *                      Pointer register (gB)
            3    IN2_rI_OFFSET void *                        Pointer (rI) specifying the offset from the
                                                             base pointer
            4    IN2_PART       uint8         LOW,HIGH       Word part which is used for operand 3

            5
                                                             Word part which is used for the result
                 OUT_PART       uint8         LOW,HIGH

operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_v40_clone_u_rowstr (ew_8w, ptrBase, ptrModify, LOW, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_pm_imm_v40_clone_u_rowstr
name        vldw_pm_imm_v40_str1_u_rowstr

Spec        vldw {ew [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                            Determines the element size and number
                               EW_options
            1    EW
                               enum                         of loaded elements (see enum definition
                                                            at vec-mem-modes.h)
            2    IN1_PTR       void *                       Pointer register (rN)
Operands
                                               31   31      32 bit immediate post modification in
            3    IN2_IMM32_6 int32           -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
            4    OUT_PART      uint8         LOW,HIGH
                                                            operand
            void* ptr;
            vec40_t vRes;
C example   ...
            vRes = vldw_pm_imm_v40_clone_u_rowstr (ew_8w, ptr, 2, LOW);

                 The same data will be loaded to all vector units (Unless str1 is configured
Comments    1.
                 otherwise).



Intrinsic   vldw_pm_ptr_v40_clone_u_rowstr
name        vldw_pm_ptr_v40_str1_u_rowstr

Spec        vldw {ew [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                EW_options
              1    EW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)

Operands      2    IN1_PTR      void *                        Pointer register (rN)
              3    IN2_PM_PTR void*                           Pointer register (rN)
                                                              Word part which is used for the result

4    OUT_PART     uint8          LOW,HIGH
                                                              operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_u_rowstr (ew_8w, ptr, vRes, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_v40_clone_u_rowstr
name          vldw_v40_str1_u_rowstr

Spec syntax   vldw {ew [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return        vec40_t
type
                                                              Determines the element size and number
                                EW_options
              1    EW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands      2    IN1_PTR      void *                        Pointer register (rN)
                                                              Word part which is used for the result
              3    OUT_PART     uint8         LOW,HIGH
                                                              operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_clone_u_rowstr (ew_8w, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_u
vldw_indexed_imm_v40_u
vldw_indexed_rI_pm_imm_v40_u
vldw_indexed_rI_pm_ptr_v40_u
vldw_indexed_rI_v40_u
vldw_indexed_rIp_pm_imm_v40_u
vldw_indexed_rIp_pm_ptr_v40_u
vldw_indexed_rIp_v40_u
vldw_pm_imm_v40_u
vldw_pm_ptr_v40_u
vldw_v40_u
Intrinsic     vldw_direct_v40_u
name
Spec syntax   vldw {ew [,u][,strX]} [#address], voz[0]l [,?prSC]

Return        vec40_t
type
                                                               Determines the element size and number
                                EW_options
              1   EW
                                enum                           of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
Operands                                          32
              2   IN1_ADDR      int32         0..2 -1          32 bit address

Word part which is used for the result
              3   OUT_PART      uint8         LOW,HIGH
                                                               operand
              vec40_t vRes;
C example     ...
              vRes = vldw_direct_v40_u (ew_8w, 2, LOW);

Comments



Intrinsic     vldw_indexed_imm_v40_u
name
Spec          vldw {ew [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]
syntax
Return        vec40_t
type
                                                               Determines the element size and number
                                 EW_options
              1   EW
                                 enum                          of loaded elements (see enum definition
                                                               at vec-mem-modes.h)
              2   IN1_gB_BASE void *                           Pointer register (gB)
Operands
                                                -              16 bit immediate post modification in
              3   IN2_IMM16_6    int16
                                                32768..32767   bytes

              4
                                                               Word part which is used for the result
                  OUT_PART       uint8          LOW,HIGH
                                                               operand
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_u (ew_8w, ptrBase, 2, LOW);

Comments



Intrinsic     vldw_indexed_rI_pm_imm_v40_u
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
Operands    3 IN2_rI_OFFSET void *
                                                              base pointer
                                                 31   31      32 bit immediate post modification in
            4 IN3_PM_IMM         int32         -2 ..2 -1

bytes
                                                              Word part which is used for the result
            5 OUT_PART           uint8         LOW,HIGH
                                                              operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_imm_v40_u (ew_8w, ptrBase, ptrModify, 2, LOW);

Comments



Intrinsic   vldw_indexed_rI_pm_ptr_v40_u
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE        void *                       Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                              base pointer
            4 IN3_PM_PTR         void*                        Pointer register (rN)

            5 OUT_PART
                                                              Word part which is used for the result
                                 uint8         LOW,HIGH
                                                              operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_ptr_v40_u (ew_8w, ptrBase, ptrModify, ptr, LOW);

Comments



Intrinsic   vldw_indexed_rI_v40_u
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE        void *                       Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the

3 IN2_rI_OFFSET void *
                                                              base pointer
                                                              Word part which is used for the result
            4 OUT_PART           uint8         LOW,HIGH
                                                              operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_v40_u (ew_8w, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vldw_indexed_rIp_pm_imm_v40_u
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition
Operands                                                      at vec-mem-modes.h)
            2 IN1_gB_BASE        void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                             base pointer
            4 IN2_PART          uint8          LOW,HIGH      Word part which is used for operand 3

            5 IN3_PM_IMM                         31   31     32 bit immediate post modification in
                                int32          -2 ..2 -1
                                                             bytes
                                                             Word part which is used for the result
            6 OUT_PART          uint8          LOW,HIGH
                                                             operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_imm_v40_u (ew_8w, ptrBase, ptrModify, LOW, 2, LOW);

Comments



Intrinsic   vldw_indexed_rIp_pm_ptr_v40_u
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1 EW
                                enum                         of loaded elements (see enum definition

at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
Operands                                                     base pointer
            4 IN2_PART          uint8          LOW,HIGH      Word part which is used for operand 3
            5 IN3_PM_PTR        void*                        Pointer register (rN)
                                                             Word part which is used for the result
            6 OUT_PART          uint8          LOW,HIGH
                                                             operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_ptr_v40_u (ew_8w, ptrBase, ptrModify, LOW, ptr, LOW);

Comments
Intrinsic   vldw_indexed_rIp_v40_u
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1 EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                       Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                             base pointer
            4 IN2_PART          uint8          LOW,HIGH      Word part which is used for operand 3
                                                             Word part which is used for the result
            5 OUT_PART          uint8          LOW,HIGH
                                                             operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_v40_u (ew_8w, ptrBase, ptrModify, LOW, LOW);

Comments



Intrinsic   vldw_pm_imm_v40_u
name
Spec        vldw {ew [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number

EW_options
            1   EW
                               enum                          of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2   IN1_PTR        void *                        Pointer register (rN)
Operands
                                                31   31      32 bit immediate post modification in
            3   IN2_IMM32_6 int32             -2 ..2 -1
                                                             bytes
                                                             Word part which is used for the result
            4   OUT_PART       uint8          LOW,HIGH
                                                             operand
            void* ptr;
C example   vec40_t vRes;
              ...
              vRes = vldw_pm_imm_v40_u (ew_8w, ptr, 2, LOW);

Comments



Intrinsic     vldw_pm_ptr_v40_u
name
Spec          vldw {ew [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]
syntax
Return        vec40_t
type
                                                                 Determines the element size and number
                                 EW_options
              1   EW
                                 enum                            of loaded elements (see enum definition
                                                                 at vec-mem-modes.h)

Operands      2   IN1_PTR        void *                          Pointer register (rN)
              3   IN2_PM_PTR void*                               Pointer register (rN)
                                                                 Word part which is used for the result
              4   OUT_PART       uint8         LOW,HIGH
                                                                 operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_u (ew_8w, ptr, vRes, LOW);

Comments



Intrinsic     vldw_v40_u
name
Spec syntax   vldw {ew [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return        vec40_t
type
                                                                 Determines the element size and number
                                EW_options
              1   EW
                                enum                             of loaded elements (see enum definition
                                                                 at vec-mem-modes.h)

Operands      2   IN1_PTR       void *                           Pointer register (rN)
                                                                 Word part which is used for the result
              3   OUT_PART      uint8         LOW,HIGH
                                                                 operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_u (ew_8w, ptr, LOW);
Comments


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_u_rowstr
vldw_indexed_rI_pm_imm_v40_u_rowstr
vldw_indexed_rI_pm_ptr_v40_u_rowstr
vldw_indexed_rI_v40_u_rowstr
vldw_indexed_rIp_pm_imm_v40_u_rowstr
vldw_indexed_rIp_pm_ptr_v40_u_rowstr
vldw_indexed_rIp_v40_u_rowstr
vldw_pm_imm_v40_u_rowstr
vldw_pm_ptr_v40_u_rowstr
vldw_v40_u_rowstr
Intrinsic   vldw_indexed_imm_v40_u_rowstr
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                EW_options
            1   EW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2   IN1_gB_BASE void *                            Pointer register (gB)
Operands
                                              -               16 bit immediate post modification in
            3   IN2_IMM16_6     int16
                                              32768..32767    bytes
                                                              Word part which is used for the result
            4   OUT_PART        uint8         LOW,HIGH
                                                              operand
            void* ptrBase;
            vec40_t vRes;
C example   ...
            vRes = vldw_indexed_imm_v40_u_rowstr (ew_8w, ptrBase, 2, LOW);

Comments



Intrinsic   vldw_indexed_rI_pm_imm_v40_u_rowstr
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition

at vec-mem-modes.h)
            2 IN1_gB_BASE        void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
Operands    3 IN2_rI_OFFSET void *
                                                              base pointer

            4 IN3_PM_IMM                         31   31      32 bit immediate post modification in
                                 int32         -2 ..2 -1
                                                              bytes
                                                              Word part which is used for the result
            5 OUT_PART           uint8         LOW,HIGH
                                                              operand
            void* ptrBase;
C example   void* ptrModify;
            vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_imm_v40_u_rowstr (ew_8w, ptrBase, ptrModify, 2, LOW);

Comments



Intrinsic   vldw_indexed_rI_pm_ptr_v40_u_rowstr
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                              Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
            2 IN1_gB_BASE        void *                       Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                              base pointer
            4 IN3_PM_PTR         void*                        Pointer register (rN)
                                                              Word part which is used for the result
            5 OUT_PART           uint8         LOW,HIGH
                                                              operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_pm_ptr_v40_u_rowstr (ew_8w, ptrBase, ptrModify, ptr, LOW);

Comments



Intrinsic   vldw_indexed_rI_v40_u_rowstr
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type

Determines the element size and number
                                 EW_options
            1 EW
                                 enum                         of loaded elements (see enum definition
Operands                                                      at vec-mem-modes.h)
            2 IN1_gB_BASE        void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                             base pointer
                                                             Word part which is used for the result
            4 OUT_PART          uint8          LOW,HIGH
                                                             operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rI_v40_u_rowstr (ew_8w, ptrBase, ptrModify, LOW);

Comments



Intrinsic   vldw_indexed_rIp_pm_imm_v40_u_rowstr
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1 EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
Operands                                                     base pointer
            4 IN2_PART          uint8          LOW,HIGH      Word part which is used for operand 3
                                                 31   31     32 bit immediate post modification in
            5 IN3_PM_IMM        int32          -2 ..2 -1
                                                             bytes
                                                             Word part which is used for the result
            6 OUT_PART          uint8          LOW,HIGH
                                                             operand
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...

vRes = vldw_indexed_rIp_pm_imm_v40_u_rowstr (ew_8w, ptrBase, ptrModify, LOW, 2, LOW);

Comments



Intrinsic   vldw_indexed_rIp_pm_ptr_v40_u_rowstr
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1 EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
Operands                                                     base pointer
            4 IN2_PART          uint8          LOW,HIGH      Word part which is used for operand 3
            5 IN3_PM_PTR        void*                        Pointer register (rN)
                                                             Word part which is used for the result
            6 OUT_PART          uint8          LOW,HIGH
                                                             operand
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_pm_ptr_v40_u_rowstr (ew_8w, ptrBase, ptrModify, LOW, ptr, LOW);

Comments



Intrinsic   vldw_indexed_rIp_v40_u_rowstr
name
Spec        vldw {ew [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                             Determines the element size and number
                                EW_options
            1 EW
                                enum                         of loaded elements (see enum definition
                                                             at vec-mem-modes.h)
            2 IN1_gB_BASE       void *                       Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
            3 IN2_rI_OFFSET void *
                                                             base pointer
            4 IN2_PART          uint8          LOW,HIGH      Word part which is used for operand 3

            5 OUT_PART

Word part which is used for the result
                                uint8          LOW,HIGH
                                                             operand
            void* ptrBase;
C example   void* ptrModify;
            vec40_t vRes;
            ...
            vRes = vldw_indexed_rIp_v40_u_rowstr (ew_8w, ptrBase, ptrModify, LOW, LOW);

Comments



Intrinsic   vldw_pm_imm_v40_u_rowstr
name
Spec        vldw {ew [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                            Determines the element size and number
                               EW_options
            1   EW
                               enum                         of loaded elements (see enum definition
                                                            at vec-mem-modes.h)
            2   IN1_PTR        void *                       Pointer register (rN)
Operands
                                               31   31      32 bit immediate post modification in
            3   IN2_IMM32_6 int32            -2 ..2 -1
                                                            bytes

            4
                                                            Word part which is used for the result
                OUT_PART       uint8         LOW,HIGH
                                                            operand
            void* ptr;
            vec40_t vRes;
C example   ...
            vRes = vldw_pm_imm_v40_u_rowstr (ew_8w, ptr, 2, LOW);

Comments



Intrinsic   vldw_pm_ptr_v40_u_rowstr
name
Spec        vldw {ew [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]
syntax
Return      vec40_t
type
                                                            Determines the element size and number
                               EW_options
            1   EW
                               enum                         of loaded elements (see enum definition
                                                            at vec-mem-modes.h)
Operands    2   IN1_PTR        void *                       Pointer register (rN)
            3   IN2_PM_PTR void*                            Pointer register (rN)
            4   OUT_PART       uint8         LOW,HIGH       Word part which is used for the result
                                                              operand
              void* ptr;
              void* vRes;
C example     ...

ptr = vldw_pm_ptr_v40_u_rowstr (ew_8w, ptr, vRes, LOW);

Comments



Intrinsic     vldw_v40_u_rowstr
name
Spec syntax   vldw {ew [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return        vec40_t
type
                                                              Determines the element size and number
                                EW_options
              1   EW
                                enum                          of loaded elements (see enum definition
                                                              at vec-mem-modes.h)
Operands      2   IN1_PTR       void *                        Pointer register (rN)
                                                              Word part which is used for the result
              3   OUT_PART      uint8         LOW,HIGH
                                                              operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_u_rowstr (ew_8w, ptr, LOW);

Comments


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_2w_dup_u
vldw_indexed_imm_v40_2w_dup_u
vldw_indexed_rI_pm_imm_v40_2w_dup_u
vldw_indexed_rI_pm_ptr_v40_2w_dup_u
vldw_indexed_rI_v40_2w_dup_u
vldw_indexed_rIp_pm_imm_v40_2w_dup_u
vldw_indexed_rIp_pm_ptr_v40_2w_dup_u
vldw_indexed_rIp_v40_2w_dup_u
vldw_pm_imm_v40_2w_dup_u
vldw_pm_ptr_v40_2w_dup_u
vldw_v40_2w_dup_u
Intrinsic     vldw_direct_v40_2w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX]} [#address], voz[0]l [,?prSC]

Return type   vec40_t
                                               32
              1    IN1_ADDR       int32     0..2 -1         32 bit address
Operands                                                    Word part which is used for the result
              2    OUT_PART       uint8     LOW,HIGH
                                                            operand
              vec40_t vRes;
C example     ...
              vRes = vldw_direct_v40_2w_dup_u (2, LOW);

Comments



Intrinsic     vldw_indexed_imm_v40_2w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE void *                        Pointer register (gB)
                                                            16 bit immediate post modification in
              2   IN2_IMM16_6      int16    -32768..32767

Operands                                                    bytes
                                                            Word part which is used for the result
              3   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_2w_dup_u (ptrBase, 2, LOW);

Comments



Intrinsic     vldw_indexed_rI_pm_imm_v40_2w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                              31    31      32 bit immediate post modification in
              3   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              4   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_2w_dup_u (ptrBase, ptrModify, 2, LOW);

Comments



Intrinsic     vldw_indexed_rI_pm_ptr_v40_2w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3   IN3_PM_PTR       void*                    Pointer register (rN)
                                                            Word part which is used for the result
              4   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...

vRes = vldw_indexed_rI_pm_ptr_v40_2w_dup_u (ptrBase, ptrModify, ptr, LOW);

Comments



Intrinsic     vldw_indexed_rI_v40_2w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                                            Word part which is used for the result
              3   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
C example     void* ptrModify;
              vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_2w_dup_u (ptrBase, ptrModify, LOW);

Comments



Intrinsic     vldw_indexed_rIp_pm_imm_v40_2w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
Operands
              4                               31   31       32 bit immediate post modification in
                   IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              5    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_2w_dup_u (ptrBase, ptrModify, LOW, 2, LOW);

Comments



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_2w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)

Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands      3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
                                                            Word part which is used for the result
              5    OUT_PART        uint8    LOW,HIGH
                                                            operand
C example     void* ptr;
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_2w_dup_u (ptrBase, ptrModify, LOW, ptr, LOW);

Comments



Intrinsic     vldw_indexed_rIp_v40_2w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                                            Word part which is used for the result
              4   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_2w_dup_u (ptrBase, ptrModify, LOW, LOW);

Comments



Intrinsic     vldw_pm_imm_v40_2w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
                                             31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
Operands                                                   bytes
                                                           Word part which is used for the result
              3    OUT_PART       uint8     LOW,HIGH
                                                           operand
              void* ptr;

vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_2w_dup_u (ptr, 2, LOW);

Comments
Intrinsic     vldw_pm_ptr_v40_2w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
Operands
                                                           Word part which is used for the result
              3    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_2w_dup_u (ptr, vRes, LOW);

Comments



Intrinsic     vldw_v40_2w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands                                                   Word part which is used for the result
              2    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_2w_dup_u (ptr, LOW);

Comments


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_2w_dup_u_rowstr
vldw_indexed_rI_pm_imm_v40_2w_dup_u_rowstr
vldw_indexed_rI_pm_ptr_v40_2w_dup_u_rowstr
vldw_indexed_rI_v40_2w_dup_u_rowstr
vldw_indexed_rIp_pm_imm_v40_2w_dup_u_rowstr
vldw_indexed_rIp_pm_ptr_v40_2w_dup_u_rowstr
vldw_indexed_rIp_v40_2w_dup_u_rowstr
vldw_pm_imm_v40_2w_dup_u_rowstr
vldw_pm_ptr_v40_2w_dup_u_rowstr
vldw_v40_2w_dup_u_rowstr
Intrinsic     vldw_indexed_imm_v40_2w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE void *                        Pointer register (gB)
                                                            16 bit immediate post modification in
              2   IN2_IMM16_6      int16    -32768..32767
Operands                                                    bytes
                                                            Word part which is used for the result
              3   OUT_PART         uint8    LOW,HIGH

operand
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_2w_dup_u_rowstr (ptrBase, 2, LOW);

Comments



Intrinsic     vldw_indexed_rI_pm_imm_v40_2w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands                                      31   31       32 bit immediate post modification in
              3   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              4   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_2w_dup_u_rowstr (ptrBase, ptrModify, 2, LOW);

Comments



Intrinsic     vldw_indexed_rI_pm_ptr_v40_2w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t
              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3   IN3_PM_PTR       void*                    Pointer register (rN)
                                                            Word part which is used for the result
              4   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_2w_dup_u_rowstr (ptrBase, ptrModify, ptr, LOW);

Comments



Intrinsic     vldw_indexed_rI_v40_2w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                                            Word part which is used for the result
              3   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_2w_dup_u_rowstr (ptrBase, ptrModify, LOW);

Comments



Intrinsic     vldw_indexed_rIp_pm_imm_v40_2w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                              31   31       32 bit immediate post modification in
              4   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes

              5
                                                            Word part which is used for the result
                  OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_2w_dup_u_rowstr (ptrBase, ptrModify, LOW, 2, LOW);

Comments



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_2w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer

Operands      3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4   IN3_PM_PTR       void*                    Pointer register (rN)
                                                            Word part which is used for the result
              5   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_2w_dup_u_rowstr (ptrBase, ptrModify, LOW, ptr, LOW);

Comments



Intrinsic     vldw_indexed_rIp_v40_2w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
Operands
              2   IN2_rI_OFFSET void *                      Pointer (rI) specifying the offset from the
                                                           base pointer
              3   IN2_PART         uint8    LOW,HIGH       Word part which is used for operand 2

              4
                                                           Word part which is used for the result
                  OUT_PART         uint8    LOW,HIGH
                                                           operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_2w_dup_u_rowstr (ptrBase, ptrModify, LOW, LOW);

Comments



Intrinsic     vldw_pm_imm_v40_2w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
                                             31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32       -2 ..2 -1
Operands                                                   bytes
                                                           Word part which is used for the result
              3    OUT_PART       uint8    LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_2w_dup_u_rowstr (ptr, 2, LOW);

Comments



Intrinsic     vldw_pm_ptr_v40_2w_dup_u_rowstr
name

Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
Operands
              3
                                                           Word part which is used for the result
                   OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_2w_dup_u_rowstr (ptr, vRes, LOW);
Comments



Intrinsic     vldw_v40_2w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                     Pointer register (rN)
Operands                                                    Word part which is used for the result
              2    OUT_PART      uint8     LOW,HIGH
                                                            operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_2w_dup_u_rowstr (ptr, LOW);

Comments


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_4w_dup_u
vldw_indexed_imm_v40_4w_dup_u
vldw_indexed_rI_pm_imm_v40_4w_dup_u
vldw_indexed_rI_pm_ptr_v40_4w_dup_u
vldw_indexed_rI_v40_4w_dup_u
vldw_indexed_rIp_pm_imm_v40_4w_dup_u
vldw_indexed_rIp_pm_ptr_v40_4w_dup_u
vldw_indexed_rIp_v40_4w_dup_u
vldw_pm_imm_v40_4w_dup_u
vldw_pm_ptr_v40_4w_dup_u
vldw_v40_4w_dup_u
Intrinsic     vldw_direct_v40_4w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX]} [#address], voz[0]l [,?prSC]

Return type   vec40_t
                                               32
              1    IN1_ADDR       int32     0..2 -1         32 bit address
Operands                                                    Word part which is used for the result
              2    OUT_PART       uint8     LOW,HIGH
                                                            operand
              vec40_t vRes;
C example     ...
              vRes = vldw_direct_v40_4w_dup_u (2, LOW);

Comments



Intrinsic     vldw_indexed_imm_v40_4w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]

Return type   vec40_t

1   IN1_gB_BASE void *                        Pointer register (gB)
                                                            16 bit immediate post modification in
              2   IN2_IMM16_6      int16    -32768..32767
Operands                                                    bytes
                                                            Word part which is used for the result
              3   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_4w_dup_u (ptrBase, 2, LOW);

Comments



Intrinsic     vldw_indexed_rI_pm_imm_v40_4w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                              31    31      32 bit immediate post modification in
              3   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              4   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_4w_dup_u (ptrBase, ptrModify, 2, LOW);

Comments



Intrinsic     vldw_indexed_rI_pm_ptr_v40_4w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3   IN3_PM_PTR       void*                    Pointer register (rN)
                                                            Word part which is used for the result
              4   OUT_PART         uint8    LOW,HIGH

operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_4w_dup_u (ptrBase, ptrModify, ptr, LOW);

Comments



Intrinsic     vldw_indexed_rI_v40_4w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                                            Word part which is used for the result
              3   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
C example     void* ptrModify;
              vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_4w_dup_u (ptrBase, ptrModify, LOW);

Comments



Intrinsic     vldw_indexed_rIp_pm_imm_v40_4w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
Operands
              4                               31   31       32 bit immediate post modification in
                   IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              5    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_4w_dup_u (ptrBase, ptrModify, LOW, 2, LOW);

Comments



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_4w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands      3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
                                                            Word part which is used for the result
              5    OUT_PART        uint8    LOW,HIGH
                                                            operand
C example     void* ptr;
              void* ptrBase;
              void* ptrModify;
              vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_4w_dup_u (ptrBase, ptrModify, LOW, ptr, LOW);

Comments



Intrinsic     vldw_indexed_rIp_v40_4w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                                            Word part which is used for the result
              4   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_4w_dup_u (ptrBase, ptrModify, LOW, LOW);

Comments



Intrinsic     vldw_pm_imm_v40_4w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
                                             31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
Operands                                                   bytes
                                                           Word part which is used for the result

3    OUT_PART       uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_4w_dup_u (ptr, 2, LOW);

Comments
Intrinsic     vldw_pm_ptr_v40_4w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
Operands
                                                           Word part which is used for the result
              3    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_4w_dup_u (ptr, vRes, LOW);

Comments



Intrinsic     vldw_v40_4w_dup_u
name
Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands                                                   Word part which is used for the result
              2    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_4w_dup_u (ptr, LOW);

Comments


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_4w_dup_u_rowstr
vldw_indexed_rI_pm_imm_v40_4w_dup_u_rowstr
vldw_indexed_rI_pm_ptr_v40_4w_dup_u_rowstr
vldw_indexed_rI_v40_4w_dup_u_rowstr
vldw_indexed_rIp_pm_imm_v40_4w_dup_u_rowstr
vldw_indexed_rIp_pm_ptr_v40_4w_dup_u_rowstr
vldw_indexed_rIp_v40_4w_dup_u_rowstr
vldw_pm_imm_v40_4w_dup_u_rowstr
vldw_pm_ptr_v40_4w_dup_u_rowstr
vldw_v40_4w_dup_u_rowstr
Intrinsic     vldw_indexed_imm_v40_4w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE void *                        Pointer register (gB)
                                                            16 bit immediate post modification in
              2   IN2_IMM16_6      int16    -32768..32767
Operands                                                    bytes

Word part which is used for the result
              3   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_4w_dup_u_rowstr (ptrBase, 2, LOW);

Comments



Intrinsic     vldw_indexed_rI_pm_imm_v40_4w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands                                      31   31       32 bit immediate post modification in
              3   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              4   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_4w_dup_u_rowstr (ptrBase, ptrModify, 2, LOW);

Comments



Intrinsic     vldw_indexed_rI_pm_ptr_v40_4w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t
              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3   IN3_PM_PTR       void*                    Pointer register (rN)
                                                            Word part which is used for the result
              4   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_4w_dup_u_rowstr (ptrBase, ptrModify, ptr, LOW);

Comments

Intrinsic     vldw_indexed_rI_v40_4w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                                            Word part which is used for the result
              3   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_4w_dup_u_rowstr (ptrBase, ptrModify, LOW);

Comments



Intrinsic     vldw_indexed_rIp_pm_imm_v40_4w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                            base pointer
              3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                              31   31       32 bit immediate post modification in
              4   IN3_PM_IMM       int32    -2 ..2 -1
                                                            bytes

              5
                                                            Word part which is used for the result
                  OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_4w_dup_u_rowstr (ptrBase, ptrModify, LOW, 2, LOW);

Comments



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_4w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the

2   IN2_rI_OFFSET void *
                                                            base pointer
Operands      3   IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4   IN3_PM_PTR       void*                    Pointer register (rN)
                                                            Word part which is used for the result
              5   OUT_PART         uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_4w_dup_u_rowstr (ptrBase, ptrModify, LOW, ptr, LOW);

Comments



Intrinsic     vldw_indexed_rIp_v40_4w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1   IN1_gB_BASE      void *                   Pointer register (gB)
Operands
              2   IN2_rI_OFFSET void *                      Pointer (rI) specifying the offset from the
                                                           base pointer
              3   IN2_PART         uint8    LOW,HIGH       Word part which is used for operand 2

              4
                                                           Word part which is used for the result
                  OUT_PART         uint8    LOW,HIGH
                                                           operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_4w_dup_u_rowstr (ptrBase, ptrModify, LOW, LOW);

Comments



Intrinsic     vldw_pm_imm_v40_4w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
                                             31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32       -2 ..2 -1
Operands                                                   bytes
                                                           Word part which is used for the result
              3    OUT_PART       uint8    LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...

vRes = vldw_pm_imm_v40_4w_dup_u_rowstr (ptr, 2, LOW);

Comments



Intrinsic     vldw_pm_ptr_v40_4w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
Operands
              3
                                                           Word part which is used for the result
                   OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_4w_dup_u_rowstr (ptr, vRes, LOW);
Comments



Intrinsic     vldw_v40_4w_dup_u_rowstr
name
Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                     Pointer register (rN)
Operands                                                    Word part which is used for the result
              2    OUT_PART      uint8     LOW,HIGH
                                                            operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_4w_dup_u_rowstr (ptr, LOW);

Comments


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_clone_2w_dup_u
vldw_indexed_imm_v40_clone_2w_dup_u
vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u
vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u
vldw_indexed_rI_v40_clone_2w_dup_u
vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u
vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u
vldw_indexed_rIp_v40_clone_2w_dup_u
vldw_pm_imm_v40_clone_2w_dup_u
vldw_pm_ptr_v40_clone_2w_dup_u
vldw_v40_clone_2w_dup_u
Intrinsic     vldw_direct_v40_clone_2w_dup_u
name          vldw_direct_v40_str1_2w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX]} [#address], voz[0]l [,?prSC]

Return type   vec40_t
                                               32
              1    IN1_ADDR       int32     0..2 -1         32 bit address
Operands                                                    Word part which is used for the result
              2    OUT_PART       uint8     LOW,HIGH
                                                            operand
              vec40_t vRes;
C example     ...

vRes = vldw_direct_v40_clone_2w_dup_u (2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_imm_v40_clone_2w_dup_u
name          vldw_indexed_imm_v40_str1_2w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                       Pointer register (gB)
                                                            16 bit immediate post modification in
              2    IN2_IMM16_6     int16    -32768..32767
Operands                                                    bytes
                                                            Word part which is used for the result
              3    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_clone_2w_dup_u (ptrBase, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u
name          vldw_indexed_rI_pm_imm_v40_str1_2w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
                                              31   31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u (ptrBase, ptrModify, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.

otherwise).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u
name          vldw_indexed_rI_pm_ptr_v40_str1_2w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN3_PM_PTR      void*                    Pointer register (rN)
                                                            Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u (ptrBase, ptrModify, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_v40_clone_2w_dup_u
name          vldw_indexed_rI_v40_str1_2w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
                                                            Word part which is used for the result
              3    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_clone_2w_dup_u (ptrBase, ptrModify, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u
name          vldw_indexed_rIp_pm_imm_v40_str1_2w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
Operands
                                              31   31       32 bit immediate post modification in
              4    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              5    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u (ptrBase, ptrModify, LOW, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u
name          vldw_indexed_rIp_pm_ptr_v40_str1_2w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)

              5
                                                            Word part which is used for the result
                   OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u (ptrBase, ptrModify, LOW, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured

Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_v40_clone_2w_dup_u
name          vldw_indexed_rIp_v40_str1_2w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
                                                            Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_clone_2w_dup_u (ptrBase, ptrModify, LOW, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_imm_v40_clone_2w_dup_u
name          vldw_pm_imm_v40_str1_2w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands                                     31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
                                                           bytes
                                                           Word part which is used for the result
              3    OUT_PART       uint8    LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_clone_2w_dup_u (ptr, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_ptr_v40_clone_2w_dup_u
name          vldw_pm_ptr_v40_str1_2w_dup_u

Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

1    IN1_PTR       void *                    Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
Operands
                                                           Word part which is used for the result
              3    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_2w_dup_u (ptr, vRes, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_v40_clone_2w_dup_u
name          vldw_v40_str1_2w_dup_u

Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands                                                   Word part which is used for the result
              2    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_clone_2w_dup_u (ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).

Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_clone_2w_dup_u_rowstr
vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u_rowstr
vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u_rowstr
vldw_indexed_rI_v40_clone_2w_dup_u_rowstr
vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u_rowstr
vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u_rowstr
vldw_indexed_rIp_v40_clone_2w_dup_u_rowstr
vldw_pm_imm_v40_clone_2w_dup_u_rowstr
vldw_pm_ptr_v40_clone_2w_dup_u_rowstr
vldw_v40_clone_2w_dup_u_rowstr
Intrinsic     vldw_indexed_imm_v40_clone_2w_dup_u_rowstr
name          vldw_indexed_imm_v40_str1_2w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                       Pointer register (gB)
                                                            16 bit immediate post modification in
              2    IN2_IMM16_6     int16    -32768..32767
Operands                                                    bytes

Word part which is used for the result
              3    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_clone_2w_dup_u_rowstr (ptrBase, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u_rowstr
name          vldw_indexed_rI_pm_imm_v40_str1_2w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands                                      31   31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_clone_2w_dup_u_rowstr (ptrBase, ptrModify, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u_rowstr
name          vldw_indexed_rI_pm_ptr_v40_str1_2w_dup_u_rowstr
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN3_PM_PTR      void*                    Pointer register (rN)

Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_clone_2w_dup_u_rowstr (ptrBase, ptrModify, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_v40_clone_2w_dup_u_rowstr
name          vldw_indexed_rI_v40_str1_2w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)

              2
                                                            Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                                            Word part which is used for the result
              3    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_clone_2w_dup_u_rowstr (ptrBase, ptrModify, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u_rowstr
name          vldw_indexed_rIp_pm_imm_v40_str1_2w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t
              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
Operands
                                              31   31       32 bit immediate post modification in
              4    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes

Word part which is used for the result
              5    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_clone_2w_dup_u_rowstr (ptrBase, ptrModify, LOW, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u_rowstr
name          vldw_indexed_rIp_pm_ptr_v40_str1_2w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands      3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
                                                            Word part which is used for the result
              5    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_clone_2w_dup_u_rowstr (ptrBase, ptrModify, LOW, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_v40_clone_2w_dup_u_rowstr
name          vldw_indexed_rIp_v40_str1_2w_dup_u_rowstr
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2

Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_clone_2w_dup_u_rowstr (ptrBase, ptrModify, LOW, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_imm_v40_clone_2w_dup_u_rowstr
name          vldw_pm_imm_v40_str1_2w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
                                             31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
Operands                                                   bytes
                                                           Word part which is used for the result
              3    OUT_PART       uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_clone_2w_dup_u_rowstr (ptr, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_ptr_v40_clone_2w_dup_u_rowstr
name          vldw_pm_ptr_v40_str1_2w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

Operands      1    IN1_PTR        void *                   Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
                                                           Word part which is used for the result
              3    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_2w_dup_u_rowstr (ptr, vRes, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_v40_clone_2w_dup_u_rowstr

name          vldw_v40_str1_2w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands                                                   Word part which is used for the result
              2    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_clone_2w_dup_u_rowstr (ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).


Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_direct_v40_clone_4w_dup_u
vldw_indexed_imm_v40_clone_4w_dup_u
vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u
vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u
vldw_indexed_rI_v40_clone_4w_dup_u
vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u
vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u
vldw_indexed_rIp_v40_clone_4w_dup_u
vldw_pm_imm_v40_clone_4w_dup_u
vldw_pm_ptr_v40_clone_4w_dup_u
vldw_v40_clone_4w_dup_u
Intrinsic     vldw_direct_v40_clone_4w_dup_u
name          vldw_direct_v40_str1_4w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX]} [#address], voz[0]l [,?prSC]

Return type   vec40_t
                                               32
              1    IN1_ADDR       int32     0..2 -1         32 bit address
Operands                                                    Word part which is used for the result
              2    OUT_PART       uint8     LOW,HIGH
                                                            operand
              vec40_t vRes;
C example     ...
              vRes = vldw_direct_v40_clone_4w_dup_u (2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_imm_v40_clone_4w_dup_u
name          vldw_indexed_imm_v40_str1_4w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                       Pointer register (gB)
                                                            16 bit immediate post modification in
              2    IN2_IMM16_6     int16    -32768..32767

Operands                                                    bytes
                                                            Word part which is used for the result
              3    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_clone_4w_dup_u (ptrBase, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u
name          vldw_indexed_rI_pm_imm_v40_str1_4w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
                                              31   31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u (ptrBase, ptrModify, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u
name          vldw_indexed_rI_pm_ptr_v40_str1_4w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN3_PM_PTR      void*                    Pointer register (rN)

Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u (ptrBase, ptrModify, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_v40_clone_4w_dup_u
name          vldw_indexed_rI_v40_str1_4w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
                                                            Word part which is used for the result
              3    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_clone_4w_dup_u (ptrBase, ptrModify, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u
name          vldw_indexed_rIp_pm_imm_v40_str1_4w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
Operands
                                              31   31       32 bit immediate post modification in
              4    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes

Word part which is used for the result
              5    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u (ptrBase, ptrModify, LOW, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u
name          vldw_indexed_rIp_pm_ptr_v40_str1_4w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
Operands                                                    Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)

              5
                                                            Word part which is used for the result
                   OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u (ptrBase, ptrModify, LOW, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_v40_clone_4w_dup_u
name          vldw_indexed_rIp_v40_str1_4w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2

Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_clone_4w_dup_u (ptrBase, ptrModify, LOW, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_imm_v40_clone_4w_dup_u
name          vldw_pm_imm_v40_str1_4w_dup_u

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
Operands                                     31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
                                                           bytes
                                                           Word part which is used for the result
              3    OUT_PART       uint8    LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_clone_4w_dup_u (ptr, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_ptr_v40_clone_4w_dup_u
name          vldw_pm_ptr_v40_str1_4w_dup_u

Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
Operands
                                                           Word part which is used for the result
              3    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_4w_dup_u (ptr, vRes, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_v40_clone_4w_dup_u
name          vldw_v40_str1_4w_dup_u

Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands                                                   Word part which is used for the result
              2    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_v40_clone_4w_dup_u (ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).

Main table → Memory Access → Load → Load unsigned W unrounded
Available addressing modes
Intrinsic Names:
vldw_indexed_imm_v40_clone_4w_dup_u_rowstr
vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u_rowstr
vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u_rowstr
vldw_indexed_rI_v40_clone_4w_dup_u_rowstr
vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u_rowstr
vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u_rowstr
vldw_indexed_rIp_v40_clone_4w_dup_u_rowstr
vldw_pm_imm_v40_clone_4w_dup_u_rowstr
vldw_pm_ptr_v40_clone_4w_dup_u_rowstr
vldw_v40_clone_4w_dup_u_rowstr
Intrinsic     vldw_indexed_imm_v40_clone_4w_dup_u_rowstr
name          vldw_indexed_imm_v40_str1_4w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+#imm16_6), voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE void *                       Pointer register (gB)
                                                            16 bit immediate post modification in
              2    IN2_IMM16_6     int16    -32768..32767
Operands                                                    bytes
                                                            Word part which is used for the result
              3    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              vec40_t vRes;
C example     ...
              vRes = vldw_indexed_imm_v40_clone_4w_dup_u_rowstr (ptrBase, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u_rowstr
name          vldw_indexed_rI_pm_imm_v40_str1_4w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands                                      31   31       32 bit immediate post modification in
              3    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_imm_v40_clone_4w_dup_u_rowstr (ptrBase, ptrModify, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u_rowstr
name          vldw_indexed_rI_pm_ptr_v40_str1_4w_dup_u_rowstr
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN3_PM_PTR      void*                    Pointer register (rN)
                                                            Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_pm_ptr_v40_clone_4w_dup_u_rowstr (ptrBase, ptrModify, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rI_v40_clone_4w_dup_u_rowstr
name          vldw_indexed_rI_v40_str1_4w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rI)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)

              2
                                                            Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
Operands                                                    base pointer
                                                            Word part which is used for the result
              3    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rI_v40_clone_4w_dup_u_rowstr (ptrBase, ptrModify, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u_rowstr
name          vldw_indexed_rIp_pm_imm_v40_str1_4w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t
              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
Operands
                                              31   31       32 bit immediate post modification in
              4    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes
                                                            Word part which is used for the result
              5    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_imm_v40_clone_4w_dup_u_rowstr (ptrBase, ptrModify, LOW, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u_rowstr

name          vldw_indexed_rIp_pm_ptr_v40_str1_4w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands      3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
                                                            Word part which is used for the result
              5    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_pm_ptr_v40_clone_4w_dup_u_rowstr (ptrBase, ptrModify, LOW, ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_indexed_rIp_v40_clone_4w_dup_u_rowstr
name          vldw_indexed_rIp_v40_str1_4w_dup_u_rowstr
Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (gB+rIp)[+pm], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
Operands
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
                                                            Word part which is used for the result
              4    OUT_PART        uint8    LOW,HIGH
                                                            operand
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vRes;
              ...
              vRes = vldw_indexed_rIp_v40_clone_4w_dup_u_rowstr (ptrBase, ptrModify, LOW, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).

Intrinsic     vldw_pm_imm_v40_clone_4w_dup_u_rowstr
name          vldw_pm_imm_v40_str1_4w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u][,strX][,rowstr]} (pN)+#imm32_6, voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR        void *                   Pointer register (rN)
                                             31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
Operands                                                   bytes
                                                           Word part which is used for the result
              3    OUT_PART       uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...
              vRes = vldw_pm_imm_v40_clone_4w_dup_u_rowstr (ptr, 2, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_pm_ptr_v40_clone_4w_dup_u_rowstr
name          vldw_pm_ptr_v40_str1_4w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

Operands      1    IN1_PTR        void *                   Pointer register (rN)
              2    IN2_PM_PTR void*                        Pointer register (rN)
                                                           Word part which is used for the result
              3    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              void* vRes;
C example     ...
              ptr = vldw_pm_ptr_v40_clone_4w_dup_u_rowstr (ptr, vRes, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vldw_v40_clone_4w_dup_u_rowstr
name          vldw_v40_str1_4w_dup_u_rowstr

Spec syntax   vldw {2w_4w, dup [,u] [,strX][,rowstr]} (pN)[+pm_x], voz[0]l [,?prSC]

Return type   vec40_t

              1    IN1_PTR       void *                    Pointer register (rN)
Operands                                                   Word part which is used for the result
              2    OUT_PART      uint8     LOW,HIGH
                                                           operand
              void* ptr;
              vec40_t vRes;
C example     ...

vRes = vldw_v40_clone_4w_dup_u_rowstr (ptr, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).


Main table → Memory Access → Load → Load unsigned W unrounded
