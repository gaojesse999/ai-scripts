# Memory Access → Load → Load coefficient

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Memory Access → Load → Load coefficient

Load coefficient

Load coefficient
Load 32 bit coefficient
Available Switches
2dw        Load two double words
int2dw When used 2dw are interleaved. The default is 4dw are interleaved.
mdw        Number of double-word loads. 1dw ≤ mdw ≤ 8dw
ndw        Number of double-word loads. 1dw ≤ ndw ≤ 4dw
           When row stride mechanism enabled - the row stride values are taken from ROWSTR0
rowstr
           or ROWSTR1 located under mod4 mode register under the following conditions:
strX       Selects the STR, PMSTR set within mod1 register and ROWSTR at mod4 register.
u          When using vozZ as destination, each vozZ which is written is zero-extended instead of
           The load operation ignores the mode-bits behavior on the vector load operation (i.e. the
vspill
           stride0/1, pmstr0/1, rowstr0/1 mode-bits are ignored - the stride is 8dw by default)
vuX        Determines the destination VCU of the instruction. X is replaced by 0 or 1.
Intrinsic Names
vlddw_c32_1dw_vuX
vlddw_c32_2dw_vuX
vlddw_c32_3dw_vuX
vlddw_c32_4dw_vuX
vlddw_c32_1dw
vlddw_c32_2dw
vlddw_c32_3dw
vlddw_c32_4dw
vlddw_c32_clone_1dw
vlddw_c32_clone_2dw
vlddw_c32_clone_3dw
vlddw_c32_clone_4dw
Instruction details in the instruction set specification
Available addressing modes
Intrinsic Names:
vlddw_c32_1dw_vuX
vlddw_pm_imm_c32_1dw_vuX
vlddw_pm_ptr_c32_1dw_vuX
Intrinsic     vlddw_c32_1dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8    0..3           Determines the destination VCU
Operands
              2    IN1_PTR        void *                  Pointer register (rN)
              void* ptr;
              coef_t vcoefRes;
C example     ...
              vcoefRes = vlddw_c32_1dw_vuX (1, ptr);

Comments



Intrinsic     vlddw_pm_imm_c32_1dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8    0..3           Determines the destination VCU

2    IN1_PTR        void *                  Pointer register (rN)
Operands
                                             31   31      32 bit immediate post modification in
              3    IN2_PM_IMM int32        -2 ..2 -1
                                                          bytes
              coef_t 2;
              void* ptr;
C example     ...
              2 = vlddw_pm_imm_c32_1dw_vuX (1, ptr, vcoefRes);

Comments



Intrinsic     vlddw_pm_ptr_c32_1dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8    0..3           Determines the destination VCU
Operands      2    IN1_PTR        void *                  Pointer register (rN)
              3    IN2_PM_PTR void*                       Pointer register (rN)
              void* ptr;
C example     void* vcoefRes;
              ...
             ptr = vlddw_pm_ptr_c32_1dw_vuX (1, ptr, vcoefRes);

Comments


Main table → Memory Access → Load → Load coefficient
Available addressing modes
Intrinsic Names:
vlddw_c32_2dw_vuX
vlddw_pm_imm_c32_2dw_vuX
vlddw_pm_ptr_c32_2dw_vuX
Intrinsic     vlddw_c32_2dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8     0..3            Determines the destination VCU
              2    IN1_PTR        void *                    Pointer register (rN)
Operands
                                                            Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                            expected)
              void* ptr;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_c32_2dw_vuX (1, ptr, vcoefRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_pm_imm_c32_2dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8     0..3            Determines the destination VCU
              2    IN1_PTR        void *                    Pointer register (rN)

Operands                                      31   31       32 bit immediate post modification in

3    IN2_PM_IMM int32         -2 ..2 -1
                                                            bytes
                                                            Coefficient result operand (register vc1 is
              4    RES2_VC1       coef_t
                                                            expected)
              coef_t 2;
              void* ptr;
C example     coef_t vcoefRes2;
              ...
              vcoefRes2 = vlddw_pm_imm_c32_2dw_vuX (1, ptr, vcoefRes1, 2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_pm_ptr_c32_2dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8     0..3            Determines the destination VCU
              2    IN1_PTR        void *                    Pointer register (rN)
Operands      3    IN2_PM_PTR void*                         Pointer register (rN)
                                                            Coefficient result operand (register vc1 is
              4    RES2_VC1       coef_t
                                                            expected)
              coef_t ptr;
              void* vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes2 = vlddw_pm_ptr_c32_2dw_vuX (1, ptr, vcoefRes1, ptr);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Memory Access → Load → Load coefficient
Available addressing modes
Intrinsic Names:
vlddw_c32_3dw_vuX
vlddw_pm_imm_c32_3dw_vuX
vlddw_pm_ptr_c32_3dw_vuX
Intrinsic     vlddw_c32_3dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
              2    IN1_PTR        void *                     Pointer register (rN)

Operands                                                     Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)

Coefficient result operand (register vc2 is
              4    RES3_VC2       coef_t
                                                             expected)
              void* ptr;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_c32_3dw_vuX (1, ptr, vcoefRes2, vcoefRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_pm_imm_c32_3dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
              2    IN1_PTR        void *                     Pointer register (rN)
                                              31   31        32 bit immediate post modification in
              3    IN2_PM_IMM int32         -2 ..2 -1
                                                             bytes
Operands
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              5    RES3_VC2       coef_t
                                                             expected)
              coef_t 2;
              void* ptr;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              ...
              vcoefRes2 = vlddw_pm_imm_c32_3dw_vuX (1, ptr, vcoefRes1, vcoefRes3, 2);

Comments      1.   This intrinsic returns more than one result. The first result variable should be
                   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_pm_ptr_c32_3dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
              2    IN1_PTR        void *                     Pointer register (rN)
              3    IN2_PM_PTR void*                          Pointer register (rN)
Operands

Coefficient result operand (register vc1 is
              4    RES2_VC1       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              5    RES3_VC2       coef_t
                                                             expected)
              coef_t ptr;
              void* vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              ...
              vcoefRes2 = vlddw_pm_ptr_c32_3dw_vuX (1, ptr, vcoefRes1, vcoefRes3, ptr);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Memory Access → Load → Load coefficient
Available addressing modes
Intrinsic Names:
vlddw_c32_4dw_vuX
vlddw_pm_imm_c32_4dw_vuX
vlddw_pm_ptr_c32_4dw_vuX
Intrinsic     vlddw_c32_4dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
              2    IN1_PTR        void *                     Pointer register (rN)
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
Operands
                                                             Coefficient result operand (register vc2 is
              4    RES3_VC2       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              5    RES4_VC3       coef_t
                                                             expected)
              void* ptr;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_c32_4dw_vuX (1, ptr, vcoefRes2, vcoefRes3, vcoefRes4);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.

Intrinsic     vlddw_pm_imm_c32_4dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
              2    IN1_PTR        void *                     Pointer register (rN)
                                              31   31        32 bit immediate post modification in
              3    IN2_PM_IMM int32         -2 ..2 -1
                                                             bytes

Operands                                                     Coefficient result operand (register vc1 is
              4    RES2_VC1       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              5    RES3_VC2       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              6    RES4_VC3       coef_t
                                                             expected)
              coef_t 2;
              void* ptr;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes2 = vlddw_pm_imm_c32_4dw_vuX (1, ptr, vcoefRes1, vcoefRes3, vcoefRes4, 2);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_pm_ptr_c32_4dw_vuX
name
Spec syntax   vlddw {ndw, vuX} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    VUX            uint8     0..3             Determines the destination VCU
              2    IN1_PTR        void *                     Pointer register (rN)
              3    IN2_PM_PTR void*                          Pointer register (rN)

              4
                                                             Coefficient result operand (register vc1 is
                   RES2_VC1       coef_t
Operands                                                     expected)
                                                             Coefficient result operand (register vc2 is
              5    RES3_VC2       coef_t

expected)
                                                             Coefficient result operand (register vc3 is
              6    RES4_VC3       coef_t
                                                             expected)
              coef_t ptr;
              void* vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes2 = vlddw_pm_ptr_c32_4dw_vuX (1, ptr, vcoefRes1, vcoefRes3, vcoefRes4, ptr);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Memory Access → Load → Load coefficient
Available addressing modes
Intrinsic Names:
vlddw_c32_1dw
vlddw_direct_c32_1dw
vlddw_indexed_imm_c32_1dw
vlddw_indexed_rI_c32_1dw
vlddw_indexed_rI_pm_imm_c32_1dw
vlddw_indexed_rI_pm_ptr_c32_1dw
vlddw_indexed_rIp_c32_1dw
vlddw_indexed_rIp_pm_imm_c32_1dw
vlddw_indexed_rIp_pm_ptr_c32_1dw
vlddw_pm_imm_c32_1dw
vlddw_pm_ptr_c32_1dw
Intrinsic     vlddw_c32_1dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

Operands      1    IN1_PTR        void *                    Pointer register (rN)
              void* ptr;
              coef_t vcoefRes;
C example     ...
              vcoefRes = vlddw_c32_1dw (ptr);

Comments



Intrinsic     vlddw_direct_c32_1dw
name
Spec syntax   vlddw {ndw [,strX]} [#address],vcZ [,?prSC]

Return type   coef_t
                                                32
Operands      1    IN1_ADDR       int32     0..2 -1         32 bit address
              coef_t vcoefRes;
C example     ...
              vcoefRes = vlddw_direct_c32_1dw (2);

Comments



Intrinsic     vlddw_indexed_imm_c32_1dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+#imm16_6),vcZ [,?prSC]

Return type   coef_t

              1   IN1_gB_BASE void *                        Pointer register (gB)
Operands                                                    16 bit immediate post modification in
              2   IN2_IMM16_6      int16    -32768..32767
                                                            bytes
              void* ptrBase;
              coef_t vcoefRes;
C example     ...
              vcoefRes = vlddw_indexed_imm_c32_1dw (ptrBase, 2);

Comments



Intrinsic     vlddw_indexed_rI_c32_1dw
name

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rI_c32_1dw (ptrBase, ptrModify);

Comments



Intrinsic     vlddw_indexed_rI_pm_imm_c32_1dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                     base pointer
                                               31   31       32 bit immediate post modification in
              3   IN3_PM_IMM        int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rI_pm_imm_c32_1dw (ptrBase, ptrModify, 2);

Comments



Intrinsic     vlddw_indexed_rI_pm_ptr_c32_1dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2   IN2_rI_OFFSET void *
                                                             base pointer
              3   IN3_PM_PTR        void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rI_pm_ptr_c32_1dw (ptrBase, ptrModify, ptr);

Comments



Intrinsic     vlddw_indexed_rIp_c32_1dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)

Pointer (rI) specifying the offset from the
Operands      2   IN2_rI_OFFSET void *
                                                             base pointer
              3   IN2_PART          uint8    LOW,HIGH        Word part which is used for operand 2
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rIp_c32_1dw (ptrBase, ptrModify, LOW);

Comments



Intrinsic     vlddw_indexed_rIp_pm_imm_c32_1dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1   IN1_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3   IN2_PART          uint8    LOW,HIGH        Word part which is used for operand 2
                                               31   31       32 bit immediate post modification in
              4   IN3_PM_IMM        int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rIp_pm_imm_c32_1dw (ptrBase, ptrModify, LOW, 2);

Comments
Intrinsic     vlddw_indexed_rIp_pm_ptr_c32_1dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1   IN1_gB_BASE       void *                  Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2   IN2_rI_OFFSET void *
Operands                                                    base pointer
              3   IN2_PART          uint8    LOW,HIGH       Word part which is used for operand 2
              4   IN3_PM_PTR        void*                   Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rIp_pm_ptr_c32_1dw (ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vlddw_pm_imm_c32_1dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)+#imm32_6,vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                    Pointer register (rN)

Operands                                      31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32         -2 ..2 -1
                                                            bytes
              void* ptr;
              coef_t vcoefRes;
C example     ...
              vcoefRes = vlddw_pm_imm_c32_1dw (ptr, 2);

Comments



Intrinsic     vlddw_pm_ptr_c32_1dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

Operands      1    IN1_PTR        void *                    Pointer register (rN)
              2    IN2_PM_PTR void*                         Pointer register (rN)
              void* ptr;
              void* vcoefRes;
C example     ...
              ptr = vlddw_pm_ptr_c32_1dw (ptr, vcoefRes);

Comments


Main table → Memory Access → Load → Load coefficient
Available addressing modes
Intrinsic Names:
vlddw_c32_2dw
vlddw_direct_c32_2dw
vlddw_indexed_imm_c32_2dw
vlddw_indexed_rI_c32_2dw
vlddw_indexed_rI_pm_imm_c32_2dw
vlddw_indexed_rI_pm_ptr_c32_2dw
vlddw_indexed_rIp_c32_2dw
vlddw_indexed_rIp_pm_imm_c32_2dw
vlddw_indexed_rIp_pm_ptr_c32_2dw
vlddw_pm_imm_c32_2dw
vlddw_pm_ptr_c32_2dw
Intrinsic     vlddw_c32_2dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                     Pointer register (rN)
Operands                                                     Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
                                                             expected)
              void* ptr;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_c32_2dw (ptr, vcoefRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_direct_c32_2dw
name
Spec syntax   vlddw {ndw [,strX]} [#address],vcZ [,?prSC]

Return type   coef_t
                                                32
              1    IN1_ADDR       int32     0..2 -1          32 bit address
Operands                                                     Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
                                                             expected)

coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     ...
              vcoefRes1 = vlddw_direct_c32_2dw (2, vcoefRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_imm_c32_2dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+#imm16_6),vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
Operands
              2    IN2_IMM16_6     int16     -32768..32767   16 bit immediate post modification in
                                                             bytes
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1        coef_t
                                                             expected)
              void* ptrBase;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_imm_c32_2dw (ptrBase, 2, vcoefRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rI_c32_2dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                     base pointer
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_rI_c32_2dw (ptrBase, ptrModify, vcoefRes2);

                   This intrinsic returns two results. The first result variable should be placed to

Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rI_pm_imm_c32_2dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
                                               31   31       32 bit immediate post modification in
              3    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_rI_pm_imm_c32_2dw (ptrBase, ptrModify, 2, vcoefRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rI_pm_ptr_c32_2dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    IN3_PM_PTR       void*                    Pointer register (rN)
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                             expected)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes1;
              coef_t vcoefRes2;
              ...

vcoefRes1 = vlddw_indexed_rI_pm_ptr_c32_2dw (ptrBase, ptrModify, ptr, vcoefRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rIp_c32_2dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t
              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_rIp_c32_2dw (ptrBase, ptrModify, LOW, vcoefRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rIp_pm_imm_c32_2dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
Operands
              4                                31   31       32 bit immediate post modification in
                   IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Coefficient result operand (register vc1 is

5    RES2_VC1         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_imm_c32_2dw (ptrBase, ptrModify, LOW, 2, vcoefRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rIp_pm_ptr_c32_2dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands      3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR       void*                    Pointer register (rN)
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1         coef_t
                                                             expected)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes1;
              coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_ptr_c32_2dw (ptrBase, ptrModify, LOW, ptr, vcoefRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_pm_imm_c32_2dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)+#imm32_6,vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                    Pointer register (rN)

              2                               31   31       32 bit immediate post modification in
                   IN2_IMM32_6 int32         -2 ..2 -1
Operands                                                    bytes
                                                            Coefficient result operand (register vc1 is

3    RES2_VC1       coef_t
                                                            expected)
              void* ptr;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_pm_imm_c32_2dw (ptr, 2, vcoefRes2);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).
Intrinsic     vlddw_pm_ptr_c32_2dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                     Pointer register (rN)
              2    IN2_PM_PTR void*                          Pointer register (rN)
Operands
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
              coef_t ptr;
              void* vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes2 = vlddw_pm_ptr_c32_2dw (ptr, vcoefRes1, ptr);

                   This intrinsic returns two results. The first result variable should be placed to
Comments      1.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).


Main table → Memory Access → Load → Load coefficient
Available addressing modes
Intrinsic Names:
vlddw_c32_3dw
vlddw_direct_c32_3dw
vlddw_indexed_imm_c32_3dw
vlddw_indexed_rI_c32_3dw
vlddw_indexed_rI_pm_imm_c32_3dw
vlddw_indexed_rI_pm_ptr_c32_3dw
vlddw_indexed_rIp_c32_3dw
vlddw_indexed_rIp_pm_imm_c32_3dw
vlddw_indexed_rIp_pm_ptr_c32_3dw
vlddw_pm_imm_c32_3dw
vlddw_pm_ptr_c32_3dw
Intrinsic     vlddw_c32_3dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                     Pointer register (rN)
                                                             Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
Operands                                                     expected)
                                                             Coefficient result operand (register vc2 is
              3    RES3_VC2       coef_t
                                                             expected)

void* ptr;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_c32_3dw (ptr, vcoefRes2, vcoefRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_direct_c32_3dw
name
Spec syntax   vlddw {ndw [,strX]} [#address],vcZ [,?prSC]

Return type   coef_t
                                                32
              1    IN1_ADDR       int32     0..2 -1          32 bit address
                                                             Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
Operands                                                     expected)

              3
                                                             Coefficient result operand (register vc2 is
                   RES3_VC2       coef_t
                                                             expected)
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_direct_c32_3dw (2, vcoefRes2, vcoefRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_imm_c32_3dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+#imm16_6),vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE void *                         Pointer register (gB)
                                                              16 bit immediate post modification in
              2    IN2_IMM16_6      int16    -32768..32767
                                                              bytes
Operands                                                      Coefficient result operand (register vc1 is
              3    RES2_VC1         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              4    RES3_VC2         coef_t
                                                              expected)
              void* ptrBase;

coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_imm_c32_3dw (ptrBase, 2, vcoefRes2, vcoefRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rI_c32_3dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)

              2
                                                              Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
                                                              base pointer
Operands                                                      Coefficient result operand (register vc1 is
              3    RES2_VC1         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              4    RES3_VC2         coef_t
                                                              expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rI_c32_3dw (ptrBase, ptrModify, vcoefRes2, vcoefRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
Intrinsic     vlddw_indexed_rI_pm_imm_c32_3dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
                                               31   31       32 bit immediate post modification in
              3    IN3_PM_IMM       int32    -2 ..2 -1
Operands                                                     bytes

Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              5    RES3_VC2         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rI_pm_imm_c32_3dw (ptrBase, ptrModify, 2, vcoefRes2, vcoefRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rI_pm_ptr_c32_3dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

              2
                                                             Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
                                                             base pointer
              3    IN3_PM_PTR       void*                    Pointer register (rN)
Operands
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                             expected)

              5
                                                             Coefficient result operand (register vc2 is
                   RES3_VC2         coef_t
                                                             expected)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rI_pm_ptr_c32_3dw (ptrBase, ptrModify, ptr, vcoefRes2, vcoefRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rIp_c32_3dw
name

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
              3    IN2_PART         uint8     LOW,HIGH        Word part which is used for operand 2
Operands
                                                              Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                              expected)

              5
                                                              Coefficient result operand (register vc2 is
                   RES3_VC2         coef_t
                                                              expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rIp_c32_3dw (ptrBase, ptrModify, LOW, vcoefRes2, vcoefRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rIp_pm_imm_c32_3dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

Operands      1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2

              4                                31   31       32 bit immediate post modification in
                   IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1         coef_t
                                                             expected)

Coefficient result operand (register vc2 is
              6    RES3_VC2         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_imm_c32_3dw (ptrBase, ptrModify, LOW, 2, vcoefRes2, vcoefRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rIp_pm_ptr_c32_3dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
Operands      4    IN3_PM_PTR       void*                    Pointer register (rN)
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1         coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              6    RES3_VC2         coef_t
                                                             expected)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_ptr_c32_3dw (ptrBase, ptrModify, LOW, ptr, vcoefRes2, vcoefRes3);
                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_pm_imm_c32_3dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)+#imm32_6,vcZ [,?prSC]

Return type   coef_t

1    IN1_PTR        void *                    Pointer register (rN)
                                             31   31        32 bit immediate post modification in
              2    IN2_IMM32_6 int32       -2 ..2 -1
                                                            bytes
Operands                                                    Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                            expected)
                                                            Coefficient result operand (register vc2 is
              4    RES3_VC2       coef_t
                                                            expected)
              void* ptr;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_pm_imm_c32_3dw (ptr, 2, vcoefRes2, vcoefRes3);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_pm_ptr_c32_3dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                    Pointer register (rN)
              2    IN2_PM_PTR void*                         Pointer register (rN)

Operands                                                    Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                            expected)
                                                            Coefficient result operand (register vc2 is
              4    RES3_VC2       coef_t
                                                            expected)
              coef_t ptr;
C example     void* vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes2 = vlddw_pm_ptr_c32_3dw (ptr, vcoefRes1, vcoefRes3, ptr);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Memory Access → Load → Load coefficient
Available addressing modes
Intrinsic Names:
vlddw_c32_4dw
vlddw_direct_c32_4dw

vlddw_indexed_imm_c32_4dw
vlddw_indexed_rI_c32_4dw
vlddw_indexed_rI_pm_imm_c32_4dw
vlddw_indexed_rI_pm_ptr_c32_4dw
vlddw_indexed_rIp_c32_4dw
vlddw_indexed_rIp_pm_imm_c32_4dw
vlddw_indexed_rIp_pm_ptr_c32_4dw
vlddw_pm_imm_c32_4dw
vlddw_pm_ptr_c32_4dw
Intrinsic     vlddw_c32_4dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                     Pointer register (rN)
                                                             Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
                                                             expected)
Operands                                                     Coefficient result operand (register vc2 is
              3    RES3_VC2       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              4    RES4_VC3       coef_t
                                                             expected)
              void* ptr;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_c32_4dw (ptr, vcoefRes2, vcoefRes3, vcoefRes4);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_direct_c32_4dw
name
Spec syntax   vlddw {ndw [,strX]} [#address],vcZ [,?prSC]

Return type   coef_t
                                                32
              1    IN1_ADDR       int32     0..2 -1          32 bit address
                                                             Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
                                                             expected)
Operands                                                     Coefficient result operand (register vc2 is
              3    RES3_VC2       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              4    RES4_VC3       coef_t
                                                             expected)

coef_t vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
C example     coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_direct_c32_4dw (2, vcoefRes2, vcoefRes3, vcoefRes4);

Comments      1.   This intrinsic returns more than one result. The first result variable should be
                   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_imm_c32_4dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+#imm16_6),vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
                                                             16 bit immediate post modification in
              2    IN2_IMM16_6     int16     -32768..32767
                                                             bytes
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1        coef_t
Operands                                                     expected)
                                                             Coefficient result operand (register vc2 is
              4    RES3_VC2        coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              5    RES4_VC3        coef_t
                                                             expected)
              void* ptrBase;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_imm_c32_4dw (ptrBase, 2, vcoefRes2, vcoefRes3, vcoefRes4);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rI_c32_4dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

              2
                                                             Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *

base pointer
Operands
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1         coef_t
                                                             expected)
              4    RES3_VC2         coef_t                   Coefficient result operand (register vc2 is
                                                              expected)
                                                              Coefficient result operand (register vc3 is
              5    RES4_VC3         coef_t
                                                              expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rI_c32_4dw (ptrBase, ptrModify, vcoefRes2, vcoefRes3, vcoefRes4);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rI_pm_imm_c32_4dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer

              3                                 31   31       32 bit immediate post modification in
                   IN3_PM_IMM       int32     -2 ..2 -1
                                                              bytes
Operands                                                      Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              5    RES3_VC2         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc3 is
              6    RES4_VC3         coef_t

expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rI_pm_imm_c32_4dw (ptrBase, ptrModify, 2, vcoefRes2, vcoefRes3,
              vcoefRes4);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
Intrinsic     vlddw_indexed_rI_pm_ptr_c32_4dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
              3    IN3_PM_PTR       void*                     Pointer register (rN)

Operands                                                      Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              5    RES3_VC2         coef_t
                                                              expected)

              6
                                                              Coefficient result operand (register vc3 is
                   RES4_VC3         coef_t
                                                              expected)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rI_pm_ptr_c32_4dw (ptrBase, ptrModify, ptr, vcoefRes2, vcoefRes3,
              vcoefRes4);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rIp_c32_4dw
name

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                      base pointer
              3    IN2_PART         uint8    LOW,HIGH         Word part which is used for operand 2
              4    RES2_VC1         coef_t                    Coefficient result operand (register vc1 is
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              5    RES3_VC2         coef_t
                                                             expected)

              6
                                                             Coefficient result operand (register vc3 is
                   RES4_VC3         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rIp_c32_4dw (ptrBase, ptrModify, LOW, vcoefRes2, vcoefRes3, vcoefRes4);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rIp_pm_imm_c32_4dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

              2
                                                             Pointer (rI) specifying the offset from the
                   IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                               31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
Operands

Coefficient result operand (register vc1 is
              5    RES2_VC1         coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              6    RES3_VC2         coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              7    RES4_VC3         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_imm_c32_4dw (ptrBase, ptrModify, LOW, 2, vcoefRes2, vcoefRes3,
              vcoefRes4);
                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rIp_pm_ptr_c32_4dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR       void*                    Pointer register (rN)
Operands
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1         coef_t
                                                             expected)

              6
                                                             Coefficient result operand (register vc2 is
                   RES3_VC2         coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              7    RES4_VC3         coef_t
                                                             expected)

void* ptr;
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_ptr_c32_4dw (ptrBase, ptrModify, LOW, ptr, vcoefRes2, vcoefRes3,
              vcoefRes4);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_pm_imm_c32_4dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)+#imm32_6,vcZ [,?prSC]

Return type   coef_t

Operands      1    IN1_PTR         void *                   Pointer register (rN)
                                              31   31        32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
                                                             bytes
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1        coef_t
                                                             expected)

              4
                                                             Coefficient result operand (register vc2 is
                   RES3_VC2        coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              5    RES4_VC3        coef_t
                                                             expected)
              void* ptr;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_pm_imm_c32_4dw (ptr, 2, vcoefRes2, vcoefRes3, vcoefRes4);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_pm_ptr_c32_4dw
name
Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                     Pointer register (rN)
              2    IN2_PM_PTR void*                          Pointer register (rN)

Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
Operands
              4
                                                             Coefficient result operand (register vc2 is
                   RES3_VC2       coef_t
                                                             expected)

              5
                                                             Coefficient result operand (register vc3 is
                   RES4_VC3       coef_t
                                                             expected)
              coef_t ptr;
              void* vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes2 = vlddw_pm_ptr_c32_4dw (ptr, vcoefRes1, vcoefRes3, vcoefRes4, ptr);

                   This intrinsic returns more than one result. The first result variable should be
Comments      1.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.

Main table → Memory Access → Load → Load coefficient
Available addressing modes
Intrinsic Names:
vlddw_c32_clone_1dw
vlddw_direct_c32_clone_1dw
vlddw_indexed_imm_c32_clone_1dw
vlddw_indexed_rI_c32_clone_1dw
vlddw_indexed_rI_pm_imm_c32_clone_1dw
vlddw_indexed_rI_pm_ptr_c32_clone_1dw
vlddw_indexed_rIp_c32_clone_1dw
vlddw_indexed_rIp_pm_imm_c32_clone_1dw
vlddw_indexed_rIp_pm_ptr_c32_clone_1dw
vlddw_pm_imm_c32_clone_1dw
vlddw_pm_ptr_c32_clone_1dw
Intrinsic     vlddw_c32_clone_1dw
name          vlddw_c32_str1_1dw

Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

Operands      1    IN1_PTR        void *                    Pointer register (rN)
              void* ptr;
              coef_t vcoefRes;
C example     ...
              vcoefRes = vlddw_c32_clone_1dw (ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_direct_c32_clone_1dw
name          vlddw_direct_c32_str1_1dw

Spec syntax   vlddw {ndw [,strX]} [#address],vcZ [,?prSC]

Return type   coef_t
                                               32
Operands      1    IN1_ADDR       int32     0..2 -1         32 bit address
              coef_t vcoefRes;
C example     ...
              vcoefRes = vlddw_direct_c32_clone_1dw (2);

The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_imm_c32_clone_1dw
name          vlddw_indexed_imm_c32_str1_1dw

Spec syntax   vlddw {ndw [,strX]} (gB+#imm16_6),vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE void *                       Pointer register (gB)
Operands                                                    16 bit immediate post modification in
              2    IN2_IMM16_6     int16    -32768..32767
                                                            bytes
              void* ptrBase;
              coef_t vcoefRes;
C example     ...
              vcoefRes = vlddw_indexed_imm_c32_clone_1dw (ptrBase, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).
Intrinsic     vlddw_indexed_rI_c32_clone_1dw
name          vlddw_indexed_rI_c32_str1_1dw

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rI_c32_clone_1dw (ptrBase, ptrModify);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_imm_c32_clone_1dw
name          vlddw_indexed_rI_pm_imm_c32_str1_1dw

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                     base pointer
                                               31   31       32 bit immediate post modification in
              3    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;

C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rI_pm_imm_c32_clone_1dw (ptrBase, ptrModify, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rI_pm_ptr_c32_clone_1dw
name          vlddw_indexed_rI_pm_ptr_c32_str1_1dw

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

Operands      1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN3_PM_PTR       void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rI_pm_ptr_c32_clone_1dw (ptrBase, ptrModify, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_c32_clone_1dw
name          vlddw_indexed_rIp_c32_str1_1dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rIp_c32_clone_1dw (ptrBase, ptrModify, LOW);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_pm_imm_c32_clone_1dw
name          vlddw_indexed_rIp_pm_imm_c32_str1_1dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                               31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rIp_pm_imm_c32_clone_1dw (ptrBase, ptrModify, LOW, 2);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_indexed_rIp_pm_ptr_c32_clone_1dw
name          vlddw_indexed_rIp_pm_ptr_c32_str1_1dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                  Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                    base pointer
              3    IN2_PART         uint8    LOW,HIGH       Word part which is used for operand 2
              4    IN3_PM_PTR       void*                   Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes;
              ...
              vcoefRes = vlddw_indexed_rIp_pm_ptr_c32_clone_1dw (ptrBase, ptrModify, LOW, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).



Intrinsic     vlddw_pm_imm_c32_clone_1dw
name          vlddw_pm_imm_c32_str1_1dw

Spec syntax   vlddw {ndw [,strX]} (pN)+#imm32_6,vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                    Pointer register (rN)
Operands                                      31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32         -2 ..2 -1
                                                            bytes
              void* ptr;
              coef_t vcoefRes;
C example     ...
              vcoefRes = vlddw_pm_imm_c32_clone_1dw (ptr, 2);

The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).
Intrinsic     vlddw_pm_ptr_c32_clone_1dw
name          vlddw_pm_ptr_c32_str1_1dw

Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                    Pointer register (rN)
Operands
              2    IN2_PM_PTR void*                         Pointer register (rN)
              void* ptr;
              void* vcoefRes;
C example     ...
              ptr = vlddw_pm_ptr_c32_clone_1dw (ptr, vcoefRes);

                   The same data will be loaded to all vector units (Unless str1 is configured
Comments      1.
                   otherwise).


Main table → Memory Access → Load → Load coefficient
Available addressing modes
Intrinsic Names:
vlddw_c32_clone_2dw
vlddw_direct_c32_clone_2dw
vlddw_indexed_imm_c32_clone_2dw
vlddw_indexed_rI_c32_clone_2dw
vlddw_indexed_rI_pm_imm_c32_clone_2dw
vlddw_indexed_rI_pm_ptr_c32_clone_2dw
vlddw_indexed_rIp_c32_clone_2dw
vlddw_indexed_rIp_pm_imm_c32_clone_2dw
vlddw_indexed_rIp_pm_ptr_c32_clone_2dw
vlddw_pm_imm_c32_clone_2dw
vlddw_pm_ptr_c32_clone_2dw
Intrinsic     vlddw_c32_clone_2dw
name          vlddw_c32_str1_2dw

Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                     Pointer register (rN)
Operands                                                     Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
                                                             expected)
              void* ptr;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_c32_clone_2dw (ptr, vcoefRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_direct_c32_clone_2dw
name          vlddw_direct_c32_str1_2dw

Spec syntax   vlddw {ndw [,strX]} [#address],vcZ [,?prSC]

Return type   coef_t
                                                32

1    IN1_ADDR       int32     0..2 -1          32 bit address
Operands                                                     Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
                                                             expected)
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     ...
              vcoefRes1 = vlddw_direct_c32_clone_2dw (2, vcoefRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_imm_c32_clone_2dw
name          vlddw_indexed_imm_c32_str1_2dw

Spec syntax   vlddw {ndw [,strX]} (gB+#imm16_6),vcZ [,?prSC]
Return type   coef_t

              1    IN1_gB_BASE void *                        Pointer register (gB)

              2
                                                             16 bit immediate post modification in
                   IN2_IMM16_6     int16     -32768..32767
Operands                                                     bytes
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1        coef_t
                                                             expected)
              void* ptrBase;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_imm_c32_clone_2dw (ptrBase, 2, vcoefRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rI_c32_clone_2dw
name          vlddw_indexed_rI_c32_str1_2dw

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
Operands                                                     base pointer
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_rI_c32_clone_2dw (ptrBase, ptrModify, vcoefRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rI_pm_imm_c32_clone_2dw
name          vlddw_indexed_rI_pm_imm_c32_str1_2dw

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands                                       31   31       32 bit immediate post modification in
              3    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_rI_pm_imm_c32_clone_2dw (ptrBase, ptrModify, 2, vcoefRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to

2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rI_pm_ptr_c32_clone_2dw
name          vlddw_indexed_rI_pm_ptr_c32_str1_2dw

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    IN3_PM_PTR       void*                    Pointer register (rN)
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                             expected)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes1;
              coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_rI_pm_ptr_c32_clone_2dw (ptrBase, ptrModify, ptr, vcoefRes2);
                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rIp_c32_clone_2dw
name          vlddw_indexed_rIp_c32_str1_2dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                                             Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;

coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_rIp_c32_clone_2dw (ptrBase, ptrModify, LOW, vcoefRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rIp_pm_imm_c32_clone_2dw
name          vlddw_indexed_rIp_pm_imm_c32_str1_2dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
                                               31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_imm_c32_clone_2dw (ptrBase, ptrModify, LOW, 2, vcoefRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_indexed_rIp_pm_ptr_c32_clone_2dw
name          vlddw_indexed_rIp_pm_ptr_c32_str1_2dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands      3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR       void*                    Pointer register (rN)

              5
                                                             Coefficient result operand (register vc1 is
                   RES2_VC1         coef_t
                                                             expected)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     coef_t vcoefRes1;
              coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_ptr_c32_clone_2dw (ptrBase, ptrModify, LOW, ptr, vcoefRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).
Intrinsic     vlddw_pm_imm_c32_clone_2dw
name          vlddw_pm_imm_c32_str1_2dw

Spec syntax   vlddw {ndw [,strX]} (pN)+#imm32_6,vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                     Pointer register (rN)
                                              31   31        32 bit immediate post modification in
              2    IN2_IMM32_6 int32        -2 ..2 -1
Operands                                                     bytes
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
              void* ptr;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes1 = vlddw_pm_imm_c32_clone_2dw (ptr, 2, vcoefRes2);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to

2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).



Intrinsic     vlddw_pm_ptr_c32_clone_2dw
name          vlddw_pm_ptr_c32_str1_2dw

Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                     Pointer register (rN)
              2    IN2_PM_PTR void*                          Pointer register (rN)
Operands
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
              coef_t ptr;
              void* vcoefRes1;
C example     coef_t vcoefRes2;
              ...
              vcoefRes2 = vlddw_pm_ptr_c32_clone_2dw (ptr, vcoefRes1, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns two results. The first result variable should be placed to
              2.   the left of the = sign (lvalue). The second result variable should be passed as
                   an additional parameter (RES2_VC1).

Main table → Memory Access → Load → Load coefficient
Available addressing modes
Intrinsic Names:
vlddw_c32_clone_3dw
vlddw_direct_c32_clone_3dw
vlddw_indexed_imm_c32_clone_3dw
vlddw_indexed_rI_c32_clone_3dw
vlddw_indexed_rI_pm_imm_c32_clone_3dw
vlddw_indexed_rI_pm_ptr_c32_clone_3dw
vlddw_indexed_rIp_c32_clone_3dw
vlddw_indexed_rIp_pm_imm_c32_clone_3dw
vlddw_indexed_rIp_pm_ptr_c32_clone_3dw
vlddw_pm_imm_c32_clone_3dw
vlddw_pm_ptr_c32_clone_3dw
Intrinsic     vlddw_c32_clone_3dw
name          vlddw_c32_str1_3dw

Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                     Pointer register (rN)
                                                             Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
Operands                                                     expected)
                                                             Coefficient result operand (register vc2 is
              3    RES3_VC2       coef_t
                                                             expected)
              void* ptr;
              coef_t vcoefRes1;
              coef_t vcoefRes2;

C example     coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_c32_clone_3dw (ptr, vcoefRes2, vcoefRes3);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_direct_c32_clone_3dw
name          vlddw_direct_c32_str1_3dw

Spec syntax   vlddw {ndw [,strX]} [#address],vcZ [,?prSC]

Return type   coef_t
                                                32
              1    IN1_ADDR       int32     0..2 -1          32 bit address

              2
                                                             Coefficient result operand (register vc1 is
                   RES2_VC1       coef_t
Operands                                                     expected)
                                                             Coefficient result operand (register vc2 is
              3    RES3_VC2       coef_t
                                                             expected)
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_direct_c32_clone_3dw (2, vcoefRes2, vcoefRes3);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments
              2.
                   This intrinsic returns more than one result. The first result variable should be
                   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_imm_c32_clone_3dw
name          vlddw_indexed_imm_c32_str1_3dw

Spec syntax   vlddw {ndw [,strX]} (gB+#imm16_6),vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
                                                             16 bit immediate post modification in
              2    IN2_IMM16_6     int16     -32768..32767
                                                             bytes
Operands                                                     Coefficient result operand (register vc1 is
              3    RES2_VC1        coef_t

expected)
                                                             Coefficient result operand (register vc2 is
              4    RES3_VC2        coef_t
                                                             expected)
              void* ptrBase;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_imm_c32_clone_3dw (ptrBase, 2, vcoefRes2, vcoefRes3);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rI_c32_clone_3dw
name          vlddw_indexed_rI_c32_str1_3dw

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
Operands                                                     Coefficient result operand (register vc1 is
              3    RES2_VC1         coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              4    RES3_VC2         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rI_c32_clone_3dw (ptrBase, ptrModify, vcoefRes2, vcoefRes3);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rI_pm_imm_c32_clone_3dw

name          vlddw_indexed_rI_pm_imm_c32_str1_3dw

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
                                               31   31        32 bit immediate post modification in
              3    IN3_PM_IMM       int32    -2 ..2 -1
Operands                                                      bytes
                                                              Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              5    RES3_VC2         coef_t
                                                              expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rI_pm_imm_c32_clone_3dw (ptrBase, ptrModify, 2, vcoefRes2, vcoefRes3);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


              vlddw_indexed_rI_pm_ptr_c32_clone_3dw
Intrinsic     vlddw_indexed_rI_pm_ptr_c32_str1_3dw
name
Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
              3    IN3_PM_PTR       void*                     Pointer register (rN)
Operands
                                                              Coefficient result operand (register vc1 is

4    RES2_VC1         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              5    RES3_VC2         coef_t
                                                              expected)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rI_pm_ptr_c32_clone_3dw (ptrBase, ptrModify, ptr, vcoefRes2, vcoefRes3);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rIp_c32_clone_3dw
name          vlddw_indexed_rIp_c32_str1_3dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
              3    IN2_PART         uint8    LOW,HIGH         Word part which is used for operand 2
Operands
                                                              Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              5    RES3_VC2         coef_t
                                                              expected)
C example     void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rIp_c32_clone_3dw (ptrBase, ptrModify, LOW, vcoefRes2, vcoefRes3);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).

Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rIp_pm_imm_c32_clone_3dw
name          vlddw_indexed_rIp_pm_imm_c32_str1_3dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2

Operands                                       31   31       32 bit immediate post modification in
              4    IN3_PM_IMM       int32    -2 ..2 -1
                                                             bytes
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1         coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              6    RES3_VC2         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_imm_c32_clone_3dw (ptrBase, ptrModify, LOW, 2, vcoefRes2,
              vcoefRes3);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
Intrinsic     vlddw_indexed_rIp_pm_ptr_c32_clone_3dw
name          vlddw_indexed_rIp_pm_ptr_c32_str1_3dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)

Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2
Operands      4    IN3_PM_PTR       void*                    Pointer register (rN)
                                                             Coefficient result operand (register vc1 is
              5    RES2_VC1         coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              6    RES3_VC2         coef_t
                                                             expected)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
C example     coef_t vcoefRes2;
              coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_ptr_c32_clone_3dw (ptrBase, ptrModify, LOW, ptr, vcoefRes2,
              vcoefRes3);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_pm_imm_c32_clone_3dw
name          vlddw_pm_imm_c32_str1_3dw

Spec syntax   vlddw {ndw [,strX]} (pN)+#imm32_6,vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                    Pointer register (rN)
                                              31   31       32 bit immediate post modification in
              2    IN2_IMM32_6 int32         -2 ..2 -1
                                                            bytes
Operands
              3
                                                            Coefficient result operand (register vc1 is
                   RES2_VC1       coef_t
                                                            expected)
              4    RES3_VC2       coef_t                    Coefficient result operand (register vc2 is
                                                             expected)
              void* ptr;
              coef_t vcoefRes1;
              coef_t vcoefRes2;

C example     coef_t vcoefRes3;
              ...
              vcoefRes1 = vlddw_pm_imm_c32_clone_3dw (ptr, 2, vcoefRes2, vcoefRes3);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_pm_ptr_c32_clone_3dw
name          vlddw_pm_ptr_c32_str1_3dw

Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                     Pointer register (rN)
              2    IN2_PM_PTR void*                          Pointer register (rN)

Operands                                                     Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              4    RES3_VC2       coef_t
                                                             expected)
              coef_t ptr;
              void* vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              ...
              vcoefRes2 = vlddw_pm_ptr_c32_clone_3dw (ptr, vcoefRes1, vcoefRes3, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Memory Access → Load → Load coefficient
Available addressing modes
Intrinsic Names:
vlddw_c32_clone_4dw
vlddw_direct_c32_clone_4dw
vlddw_indexed_imm_c32_clone_4dw
vlddw_indexed_rI_c32_clone_4dw
vlddw_indexed_rI_pm_imm_c32_clone_4dw
vlddw_indexed_rI_pm_ptr_c32_clone_4dw
vlddw_indexed_rIp_c32_clone_4dw
vlddw_indexed_rIp_pm_imm_c32_clone_4dw
vlddw_indexed_rIp_pm_ptr_c32_clone_4dw
vlddw_pm_imm_c32_clone_4dw
vlddw_pm_ptr_c32_clone_4dw
Intrinsic     vlddw_c32_clone_4dw
name          vlddw_c32_str1_4dw

Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

1    IN1_PTR        void *                     Pointer register (rN)
                                                             Coefficient result operand (register vc1 is
              2    RES2_VC1       coef_t
                                                             expected)
Operands                                                     Coefficient result operand (register vc2 is
              3    RES3_VC2       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              4    RES4_VC3       coef_t
                                                             expected)
              void* ptr;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_c32_clone_4dw (ptr, vcoefRes2, vcoefRes3, vcoefRes4);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_direct_c32_clone_4dw
name          vlddw_direct_c32_str1_4dw

Spec syntax   vlddw {ndw [,strX]} [#address],vcZ [,?prSC]

Return type   coef_t
                                                32
              1    IN1_ADDR       int32     0..2 -1          32 bit address

              2
                                                             Coefficient result operand (register vc1 is
                   RES2_VC1       coef_t
                                                             expected)
Operands                                                     Coefficient result operand (register vc2 is
              3    RES3_VC2       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              4    RES4_VC3       coef_t
                                                             expected)
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...

vcoefRes1 = vlddw_direct_c32_clone_4dw (2, vcoefRes2, vcoefRes3, vcoefRes4);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_imm_c32_clone_4dw
name          vlddw_indexed_imm_c32_str1_4dw

Spec syntax   vlddw {ndw [,strX]} (gB+#imm16_6),vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE void *                        Pointer register (gB)
                                                             16 bit immediate post modification in
              2    IN2_IMM16_6     int16     -32768..32767
                                                             bytes
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1        coef_t
Operands                                                     expected)
                                                             Coefficient result operand (register vc2 is
              4    RES3_VC2        coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              5    RES4_VC3        coef_t
                                                             expected)
              void* ptrBase;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_imm_c32_clone_4dw (ptrBase, 2, vcoefRes2, vcoefRes3, vcoefRes4);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rI_c32_clone_4dw
name          vlddw_indexed_rI_c32_str1_4dw

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer

              3
                                                              Coefficient result operand (register vc1 is
                   RES2_VC1         coef_t
Operands                                                      expected)
                                                              Coefficient result operand (register vc2 is
              4    RES3_VC2         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc3 is
              5    RES4_VC3         coef_t
                                                              expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rI_c32_clone_4dw (ptrBase, ptrModify, vcoefRes2, vcoefRes3, vcoefRes4);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rI_pm_imm_c32_clone_4dw
name          vlddw_indexed_rI_pm_imm_c32_str1_4dw

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
                                                31   31       32 bit immediate post modification in
              3    IN3_PM_IMM       int32     -2 ..2 -1
                                                              bytes
Operands                                                      Coefficient result operand (register vc1 is

4    RES2_VC1         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              5    RES3_VC2         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc3 is
              6    RES4_VC3         coef_t
                                                              expected)
C example     void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
              coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rI_pm_imm_c32_clone_4dw (ptrBase, ptrModify, 2, vcoefRes2, vcoefRes3,
              vcoefRes4);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rI_pm_ptr_c32_clone_4dw
name          vlddw_indexed_rI_pm_ptr_c32_str1_4dw

Spec syntax   vlddw {ndw [,strX]} (gB+rI)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                              base pointer
              3    IN3_PM_PTR       void*                     Pointer register (rN)

Operands      4
                                                              Coefficient result operand (register vc1 is
                   RES2_VC1         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc2 is
              5    RES3_VC2         coef_t
                                                              expected)
                                                              Coefficient result operand (register vc3 is
              6    RES4_VC3         coef_t

expected)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rI_pm_ptr_c32_clone_4dw (ptrBase, ptrModify, ptr, vcoefRes2, vcoefRes3,
              vcoefRes4);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments
                   This intrinsic returns more than one result. The first result variable should be
              2.
                   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rIp_c32_clone_4dw
name          vlddw_indexed_rIp_c32_str1_4dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART         uint8    LOW,HIGH        Word part which is used for operand 2

Operands                                                     Coefficient result operand (register vc1 is
              4    RES2_VC1         coef_t
                                                             expected)
                                                             Coefficient result operand (register vc2 is
              5    RES3_VC2         coef_t
                                                             expected)

              6
                                                             Coefficient result operand (register vc3 is
                   RES4_VC3         coef_t
                                                             expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rIp_c32_clone_4dw (ptrBase, ptrModify, LOW, vcoefRes2, vcoefRes3,
              vcoefRes4);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.

otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_indexed_rIp_pm_imm_c32_clone_4dw
name          vlddw_indexed_rIp_pm_imm_c32_str1_4dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE      void *                   Pointer register (gB)
Operands                                                     Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                             base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
                                              31   31       32 bit immediate post modification in
              4    IN3_PM_IMM      int32    -2 ..2 -1
                                                            bytes

              5
                                                            Coefficient result operand (register vc1 is
                   RES2_VC1        coef_t
                                                            expected)
                                                            Coefficient result operand (register vc2 is
              6    RES3_VC2        coef_t
                                                            expected)
                                                            Coefficient result operand (register vc3 is
              7    RES4_VC3        coef_t
                                                            expected)
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_imm_c32_clone_4dw (ptrBase, ptrModify, LOW, 2, vcoefRes2,
              vcoefRes3, vcoefRes4);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.

Intrinsic     vlddw_indexed_rIp_pm_ptr_c32_clone_4dw
name          vlddw_indexed_rIp_pm_ptr_c32_str1_4dw

Spec syntax   vlddw {ndw [,strX]} (gB+rIp)[+pm],vcZ [,?prSC]

Return type   coef_t

              1    IN1_gB_BASE     void *                   Pointer register (gB)
                                                            Pointer (rI) specifying the offset from the
              2    IN2_rI_OFFSET void *
                                                            base pointer
              3    IN2_PART        uint8    LOW,HIGH        Word part which is used for operand 2
              4    IN3_PM_PTR      void*                    Pointer register (rN)
Operands
                                                            Coefficient result operand (register vc1 is
              5    RES2_VC1        coef_t
                                                            expected)

              6
                                                            Coefficient result operand (register vc2 is
                   RES3_VC2        coef_t
                                                            expected)
                                                            Coefficient result operand (register vc3 is
              7    RES4_VC3        coef_t
                                                            expected)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_indexed_rIp_pm_ptr_c32_clone_4dw (ptrBase, ptrModify, LOW, ptr, vcoefRes2,
              vcoefRes3, vcoefRes4);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.



Intrinsic     vlddw_pm_imm_c32_clone_4dw
name          vlddw_pm_imm_c32_str1_4dw

Spec syntax   vlddw {ndw [,strX]} (pN)+#imm32_6,vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                    Pointer register (rN)
                                              31   31       32 bit immediate post modification in

2    IN2_IMM32_6 int32        -2 ..2 -1
                                                            bytes
                                                            Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
Operands                                                    expected)
                                                            Coefficient result operand (register vc2 is
              4    RES3_VC2       coef_t
                                                            expected)

              5
                                                            Coefficient result operand (register vc3 is
                   RES4_VC3       coef_t
                                                            expected)
              void* ptr;
              coef_t vcoefRes1;
              coef_t vcoefRes2;
C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes1 = vlddw_pm_imm_c32_clone_4dw (ptr, 2, vcoefRes2, vcoefRes3, vcoefRes4);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.
Intrinsic     vlddw_pm_ptr_c32_clone_4dw
name          vlddw_pm_ptr_c32_str1_4dw

Spec syntax   vlddw {ndw [,strX]} (pN)[+pm_x],vcZ [,?prSC]

Return type   coef_t

              1    IN1_PTR        void *                     Pointer register (rN)
              2    IN2_PM_PTR void*                          Pointer register (rN)
                                                             Coefficient result operand (register vc1 is
              3    RES2_VC1       coef_t
                                                             expected)
Operands
                                                             Coefficient result operand (register vc2 is
              4    RES3_VC2       coef_t
                                                             expected)
                                                             Coefficient result operand (register vc3 is
              5    RES4_VC3       coef_t
                                                             expected)
              coef_t ptr;
              void* vcoefRes1;
              coef_t vcoefRes2;

C example     coef_t vcoefRes3;
              coef_t vcoefRes4;
              ...
              vcoefRes2 = vlddw_pm_ptr_c32_clone_4dw (ptr, vcoefRes1, vcoefRes3, vcoefRes4, ptr);

                   The same data will be loaded to all vector units (Unless str1 is configured
              1.
                   otherwise).
Comments           This intrinsic returns more than one result. The first result variable should be
              2.   placed to the left of the = sign (lvalue). Additional result variables should be
                   passed as parameters.


Main table → Memory Access → Load → Load coefficient
