# Memory Access → Store → Store 32 bit double word

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Memory Access → Store → Store 32 bit double word

Store 32 bit double word

Store 32 bit double word
Store 32 bit double word
Available Switches
2dw       Store two double-words
8dw       Store eight double-words
concat Data concatenation
mdw       Number of double-word stores. 1dw ≤ mdw ≤ 8dw
ndw       Number of double-word stores. 1dw ≤ ndw ≤ 4dw

The store operation ignores the mode-bits behavior on the vector store operation (i.e. the
vspill
          vshfdw, vsatsdw, vshfl and vsatsl mode-bits are ignored - the stride is 8dw by default)
vuX       Determines the source VCU of the instruction. voz[0] ≤ vuX ≤ voz[3]
Intrinsic Names
vstdw_v32_vuX
vstdw_v40ext_2dw
vstdw_v40ext_2dw_concat
vstdw_v32
vstdw_v32_concat
vstdw_v40_vuX
vstdw_v40
vstdw_v40_concat
vstdw_v40ext_2dw_vuX
Instruction details in the instruction set specification
Available addressing modes
Intrinsic Names:
vstdw_v32_indexed_rI_pm_imm_vuX
vstdw_v32_indexed_rI_pm_ptr_vuX
vstdw_v32_indexed_rI_vuX
vstdw_v32_indexed_rIp_pm_imm_vuX
vstdw_v32_indexed_rIp_pm_ptr_vuX
vstdw_v32_indexed_rIp_vuX
vstdw_v32_pm_imm_vuX
vstdw_v32_pm_ptr_vuX
vstdw_v32_vuX
Intrinsic   vstdw_v32_indexed_rI_pm_imm_vuX
name
Spec        vstdw {mdw, vuX} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2    VUX             uint8           0..3         Determines the source VCU
            3    IN1_V32         vec_t                        Input vector operand
                                                              Offset for the first DW used from
Operands    4    IN1_OFST        uint8           0,4
                                                              operand 3
            5    IN2_gB_BASE     void *                       Pointer register (gB)

            6
                                                              Pointer (rI) specifying the offset from
                 IN3_rI_OFFSET void *
                                                              the base pointer
                                                   31   31    32 bit immediate post modification in
            7    IN4_PM_IMM      int32           -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rI_pm_imm_vuX (mdw_8dw, 1, vIn, 0, ptrBase, ptrModify, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.

vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rI_pm_ptr_vuX
name
Spec        vstdw {mdw, vuX} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 NDW_options
            1    NDW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2    VUX             uint8            0..3          Determines the source VCU
            3    IN1_V32         vec_t                          Input vector operand
Operands                                                        Offset for the first DW used from
            4    IN1_OFST        uint8            0,4
                                                                operand 3
            5    IN2_gB_BASE     void *                         Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            6    IN3_rI_OFFSET void *
                                                                base pointer
            7    IN4_PM_PTR      void*                          Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rI_pm_ptr_vuX (ndw_4dw, 1, vIn, 0, ptrBase, ptrModify, ptr);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the

2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rI_vuX
name
Spec        vstdw {mdw, vuX} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)

Operands    2    VUX             uint8            0..3          Determines the source VCU
            3    IN1_V32         vec_t                          Input vector operand
                                                                Offset for the first DW used from
            4    IN1_OFST        uint8            0,4
                                                                operand 3
            5    IN2_gB_BASE     void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from
            6    IN3_rI_OFFSET void *
                                                               the base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rI_vuX (mdw_8dw, 1, vIn, 0, ptrBase, ptrModify);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rIp_pm_imm_vuX
name
Spec        vstdw {mdw,vuX} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type

Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2    VUX             uint8            0..3         Determines the source VCU
            3    IN1_V32         vec_t                         Input vector operand
                                                               Offset for the first DW used from
            4    IN1_OFST        uint8            0,4
Operands                                                       operand 3
            5    IN2_gB_BASE     void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from
            6    IN3_rI_OFFSET void *
                                                               the base pointer
            7    IN3_PART        uint8            LOW,HIGH     Word part which is used for operand 6
                                                    31   31    32 bit immediate post modification in
            8    IN4_PM_IMM      int32            -2 ..2 -1
                                                               bytes
            void* ptrBase;
C example   void* ptrModify;
            vec_t vIn;
            ...
            vstdw_v32_indexed_rIp_pm_imm_vuX (mdw_8dw, 1, vIn, 0, ptrBase, ptrModify, LOW, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rIp_pm_ptr_vuX
name
Spec        vstdw {mdw,vuX} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 NDW_options

1    NDW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2    VUX             uint8           0..3          Determines the source VCU
            3    IN1_V32         vec_t                         Input vector operand
                                                               Offset for the first DW used from
Operands    4    IN1_OFST        uint8           0,4
                                                               operand 3
            5    IN2_gB_BASE     void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            6    IN3_rI_OFFSET void *
                                                               base pointer
            7    IN3_PART        uint8           LOW,HIGH      Word part which is used for operand 6
            8    IN4_PM_PTR      void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rIp_pm_ptr_vuX (ndw_4dw, 1, vIn, 0, ptrBase, ptrModify, LOW, ptr);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.

Comments         vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
            2.   some case, saturation might be wrongly applied if voX is allocated and DW
                 vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
                 VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rIp_vuX
name
Spec        vstdw {mdw,vuX} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

2    VUX             uint8           0..3         Determines the source VCU
            3    IN1_V32         vec_t                        Input vector operand
Operands                                                      Offset for the first DW used from
            4    IN1_OFST        uint8           0,4
                                                              operand 3
            5    IN2_gB_BASE     void *                       Pointer register (gB)

            6
                                                              Pointer (rI) specifying the offset from
                 IN3_rI_OFFSET void *
                                                              the base pointer
            7    IN3_PART        uint8           LOW,HIGH     Word part which is used for operand 6
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rIp_vuX (mdw_8dw, 1, vIn, 0, ptrBase, ptrModify, LOW);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic    vstdw_v32_pm_imm_vuX
name
Spec        vstdw {mdw, vuX} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                              MDW_options
            1    MDW
                              enum                          of stored elements (see enum definition at
                                                            vec-mem-modes.h)
            2    VUX          uint8           0..3          Determines the source VCU
            3    IN1_V32      vec_t                         Input vector operand
Operands
                                                            Offset for the first DW used from
            4    IN1_OFST     uint8           0,4

operand 3
            5    IN2_PTR      void *                        Pointer register (rN)
                                                31   31     32 bit immediate post modification in
            6    IN3_PM_IMM int32             -2 ..2 -1
                                                            bytes
            void* ptr;
            vec_t vIn;
C example   ...
            vstdw_v32_pm_imm_vuX (mdw_8dw, 1, vIn, 0, ptr, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_pm_ptr_vuX
name
Spec        vstdw {mdw, vuX} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                              NDW_options
            1    NDW
                              enum                          of stored elements (see enum definition
                                                            at vec-mem-modes.h)
Operands
            2    VUX          uint8           0..3          Determines the source VCU
            3    IN1_V32      vec_t                         Input vector operand
                                                               Offset for the first DW used from
            4    IN1_OFST      uint8            0,4
                                                               operand 3
            5    IN2_PTR       void *                          Pointer register (rN)
            6    IN3_PM_PTR void*                              Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstdw_v32_pm_ptr_vuX (ndw_4dw, 1, vIn, 0, ptr, ptr);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In

some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_vuX
name
Spec        vstdw {mdw, vuX} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                              MDW_options
            1    MDW
                              enum                             of stored elements (see enum definition at
                                                               vec-mem-modes.h)
            2    VUX          uint8            0..3            Determines the source VCU
Operands    3    IN1_V32      vec_t                            Input vector operand
                                                               Offset for the first DW used from
            4    IN1_OFST     uint8            0,4
                                                               operand 3
            5    IN2_PTR      void *                           Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstdw_v32_vuX (mdw_8dw, 1, vIn, 0, ptr);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.

Comments         vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
            2.   some case, saturation might be wrongly applied if voX is allocated and DW
                 vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
              VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
              operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
              is applicable, bind the storted vec_t variable to a viX register (less
              recommended).


Main table → Memory Access → Store → Store 32 bit double word
Available addressing modes
Intrinsic Names:
vstdw_v40ext_2dw
vstdw_v40ext_direct_2dw
vstdw_v40ext_indexed_imm_2dw
vstdw_v40ext_indexed_rI_2dw
vstdw_v40ext_indexed_rI_pm_imm_2dw
vstdw_v40ext_indexed_rI_pm_ptr_2dw

vstdw_v40ext_indexed_rIp_2dw
vstdw_v40ext_indexed_rIp_pm_imm_2dw
vstdw_v40ext_indexed_rIp_pm_ptr_2dw
vstdw_v40ext_pm_imm_2dw
vstdw_v40ext_pm_ptr_2dw
Intrinsic     vstdw_v40ext_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
Operands
              2      IN2_PTR       void *                    Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_2dw (vIn, ptr);

Comments



Intrinsic     vstdw_v40ext_direct_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, [#address] [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
Operands                                          32
              2      IN2_ADDR      int32     0..2 -1         32 bit address
              vec40_t vIn;
C example     ...
              vstdw_v40ext_direct_2dw (vIn, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_imm_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+#imm16_6) [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
              2      IN2_gB_BASE void *                      Pointer register (gB)
Operands
                                                             16 bit immediate post modification in
              3      IN3_IMM16_6   int16     -32768..32767
                                                             bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_indexed_imm_2dw (vIn, ptrBase, 2);

Comments
Intrinsic     vstdw_v40ext_indexed_rI_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_2dw (vIn, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_imm_2dw
name

Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)

Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
                                                31   31       32 bit immediate post modification in
              4   IN4_PM_IMM        int32     -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_imm_2dw (vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_ptr_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]
Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
              4   IN4_PM_PTR        void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_ptr_2dw (vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
              4   IN3_PART          uint8     LOW,HIGH        Word part which is used for operand 3
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...

vstdw_v40ext_indexed_rIp_2dw (vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_pm_imm_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
Operands
              2   IN2_gB_BASE       void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                             base pointer
              4   IN3_PART          uint8      LOW,HIGH      Word part which is used for operand 3

              5                                 31    31     32 bit immediate post modification in
                  IN4_PM_IMM        int32      -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_imm_2dw (vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_pm_ptr_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                  Output vector operand
              2   IN2_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      3   IN3_rI_OFFSET void *
                                                             base pointer
              4   IN3_PART          uint8      LOW,HIGH      Word part which is used for operand 3
              5   IN4_PM_PTR        void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_ptr_2dw (vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_v40ext_pm_imm_2dw
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (pN)+#imm32_6 [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
Operands      2      IN2_PTR       void *                    Pointer register (rN)
                                               31    31

3      IN3_IMM32_6 int32        -2 ..2 -1      32 bit immediate post modification in
                                                          bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_pm_imm_2dw (vIn, ptr, 2);

Comments



Intrinsic      vstdw_v40ext_pm_ptr_2dw
name
Spec syntax    vstdw {2dw [,concat]} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type    void

               1      IN1_V40      vec40_t                Output vector operand
Operands       2      IN2_PTR      void *                 Pointer register (rN)
               3      IN3_PM_PTR void*                    Pointer register (rN)
               void* ptr;
               vec40_t vIn;
C example      ...
               vstdw_v40ext_pm_ptr_2dw (vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 32 bit double word
Available addressing modes
Intrinsic Names:
vstdw_v40ext_2dw_concat
vstdw_v40ext_direct_2dw_concat
vstdw_v40ext_indexed_imm_2dw_concat
vstdw_v40ext_indexed_rI_2dw_concat
vstdw_v40ext_indexed_rI_pm_imm_2dw_concat
vstdw_v40ext_indexed_rI_pm_ptr_2dw_concat
vstdw_v40ext_indexed_rIp_2dw_concat
vstdw_v40ext_indexed_rIp_pm_imm_2dw_concat
vstdw_v40ext_indexed_rIp_pm_ptr_2dw_concat
vstdw_v40ext_pm_imm_2dw_concat
vstdw_v40ext_pm_ptr_2dw_concat
Intrinsic     vstdw_v40ext_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
Operands
              2      IN2_PTR       void *                    Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_2dw_concat (vIn, ptr);

Comments



Intrinsic     vstdw_v40ext_direct_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, [#address] [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand
Operands                                        32
              2      IN2_ADDR      int32     0..2 -1         32 bit address
              vec40_t vIn;
C example     ...
              vstdw_v40ext_direct_2dw_concat (vIn, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_imm_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+#imm16_6) [,?prSC]

Return type   void

              1      IN1_V40       vec40_t                   Output vector operand

2      IN2_gB_BASE void *                      Pointer register (gB)
Operands
                                                             16 bit immediate post modification in
              3      IN3_IMM16_6   int16     -32768..32767
                                                             bytes
              void* ptrBase;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_indexed_imm_2dw_concat (vIn, ptrBase, 2);

Comments
Intrinsic     vstdw_v40ext_indexed_rI_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_2dw_concat (vIn, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_imm_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)

Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
                                                31   31       32 bit immediate post modification in
              4   IN4_PM_IMM        int32     -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_imm_2dw_concat (vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_ptr_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rI)[+pm] [,?prSC]
Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)

Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
              4   IN4_PM_PTR        void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_ptr_2dw_concat (vIn, ptrBase, ptrModify, ptr);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
              2   IN2_gB_BASE       void *                    Pointer register (gB)
Operands                                                      Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                              base pointer
              4   IN3_PART          uint8     LOW,HIGH        Word part which is used for operand 3
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_2dw_concat (vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_pm_imm_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                   Output vector operand
Operands
              2   IN2_gB_BASE       void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              3   IN3_rI_OFFSET void *
                                                             base pointer
              4   IN3_PART          uint8      LOW,HIGH      Word part which is used for operand 3

              5                                 31    31     32 bit immediate post modification in
                  IN4_PM_IMM        int32      -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_imm_2dw_concat (vIn, ptrBase, ptrModify, LOW, 2);

Comments

Intrinsic     vstdw_v40ext_indexed_rIp_pm_ptr_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   IN1_V40           vec40_t                  Output vector operand
              2   IN2_gB_BASE       void *                   Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
Operands      3   IN3_rI_OFFSET void *
                                                             base pointer
              4   IN3_PART          uint8      LOW,HIGH      Word part which is used for operand 3
              5   IN4_PM_PTR        void*                    Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_ptr_2dw_concat (vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_v40ext_pm_imm_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (pN)+#imm32_6 [,?prSC]

Return type   void

              1      IN1_V40      vec40_t                   Output vector operand
Operands      2      IN2_PTR      void *                    Pointer register (rN)
                                               31    31
              3      IN3_IMM32_6 int32        -2 ..2 -1     32 bit immediate post modification in
                                                                bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_pm_imm_2dw_concat (vIn, ptr, 2);

Comments



Intrinsic     vstdw_v40ext_pm_ptr_2dw_concat
name
Spec syntax   vstdw {2dw [,concat]} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      IN1_V40      vec40_t                       Output vector operand
Operands      2      IN2_PTR      void *                        Pointer register (rN)
              3      IN3_PM_PTR void*                           Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_pm_ptr_2dw_concat (vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 32 bit double word
Available addressing modes
Intrinsic Names:
vstdw_v32
vstdw_v32_direct
vstdw_v32_indexed_imm
vstdw_v32_indexed_rI
vstdw_v32_indexed_rI_pm_imm
vstdw_v32_indexed_rI_pm_ptr
vstdw_v32_indexed_rIp
vstdw_v32_indexed_rIp_pm_imm
vstdw_v32_indexed_rIp_pm_ptr
vstdw_v32_pm_imm

vstdw_v32_pm_ptr
Intrinsic   vstdw_v32
name
Spec        vstdw {mdw [,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                          Determines the element size and number
                              MDW_options
            1    MDW
                              enum                        of stored elements (see enum definition at
                                                          vec-mem-modes.h)

Operands    2    IN1_V32      vec_t                       Input vector operand
                                                          Offset for the first DW used from
            3    IN1_OFST     uint8             0,4
                                                          operand 2
            4    IN2_PTR      void *                      Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstdw_v32 (mdw_8dw, vIn, 0, ptr);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_direct
name
Spec        vstdw {mdw [,concat]} vix[0], [#address] [,?prSC]
syntax
Return      void
type
                                                          Determines the element size and number
                              MDW_options
            1    MDW
                              enum                        of stored elements (see enum definition at
                                                          vec-mem-modes.h)
Operands    2    IN1_V32      vec_t                       Input vector operand

            3    IN1_OFST     uint8
                                                          Offset for the first DW used from
                                                0,4
                                                          operand 2
                                                     32

4    IN2_ADDR      int32          0..2 -1        32 bit address
            vec_t vIn;
C example   ...
            vstdw_v32_direct (mdw_8dw, vIn, 0, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_imm
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and
                                MDW_options
            1    MDW
                                enum                           number of stored elements (see enum
                                                               definition at vec-mem-modes.h)
            2    IN1_V32        vec_t                          Input vector operand
Operands                                                       Offset for the first DW used from
            3    IN1_OFST       uint8           0,4
                                                               operand 2
            4    IN2_gB_BASE void *                            Pointer register (gB)
                                                -              16 bit immediate post modification in
            5    IN3_IMM16_6    int16
                                                32768..32767   bytes
            void* ptrBase;
            vec_t vIn;
C example   ...
            vstdw_v32_indexed_imm (mdw_8dw, vIn, 0, ptrBase, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the

2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).
Intrinsic   vstdw_v32_indexed_rI
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2    IN1_V32         vec_t                          Input vector operand
Operands                                                        Offset for the first DW used from
            3    IN1_OFST        uint8            0,4
                                                                operand 2
            4    IN2_gB_BASE     void *                         Pointer register (gB)
                                                                Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                                the base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rI (mdw_8dw, vIn, 0, ptrBase, ptrModify);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rI_pm_imm
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type

MDW_options                    Determines the element size and number
Operands    1    MDW
                                 enum                           of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_V32         vec_t                        Input vector operand

            3
                                                              Offset for the first DW used from
                 IN1_OFST        uint8           0,4
                                                              operand 2
            4    IN2_gB_BASE     void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                              the base pointer
                                                   31   31    32 bit immediate post modification in
            6    IN4_PM_IMM      int32           -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rI_pm_imm (mdw_8dw, vIn, 0, ptrBase, ptrModify, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rI_pm_ptr
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 NDW_options
            1    NDW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)

2    IN1_V32         vec_t                        Input vector operand
Operands                                                      Offset for the first DW used from
            3    IN1_OFST        uint8           0,4
                                                              operand 2
            4    IN2_gB_BASE     void *                       Pointer register (gB)

            5    IN3_rI_OFFSET void *
                                                              Pointer (rI) specifying the offset from the
                                                              base pointer
            6    IN4_PM_PTR      void*                          Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rI_pm_ptr (ndw_4dw, vIn, 0, ptrBase, ptrModify, ptr);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rIp
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2    IN1_V32         vec_t                          Input vector operand
                                                                Offset for the first DW used from
Operands    3    IN1_OFST        uint8            0,4
                                                                operand 2
            4    IN2_gB_BASE     void *                         Pointer register (gB)

Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                                the base pointer
            6    IN3_PART        uint8            LOW,HIGH      Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rIp (mdw_8dw, vIn, 0, ptrBase, ptrModify, LOW);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
Comments         vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
            2.
                 some case, saturation might be wrongly applied if voX is allocated and DW
                 vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
                 VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rIp_pm_imm
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MDW_options
            1    MDW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_V32        vec_t                        Input vector operand
                                                             Offset for the first DW used from
            3    IN1_OFST       uint8           0,4
                                                             operand 2
Operands    4    IN2_gB_BASE    void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                             the base pointer
            6    IN3_PART       uint8           LOW,HIGH     Word part which is used for operand 5
                                                  31   31    32 bit immediate post modification in
            7    IN4_PM_IMM     int32           -2 ..2 -1

bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rIp_pm_imm (mdw_8dw, vIn, 0, ptrBase, ptrModify, LOW, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).
Intrinsic   vstdw_v32_indexed_rIp_pm_ptr
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 NDW_options
            1    NDW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2    IN1_V32         vec_t                         Input vector operand
                                                               Offset for the first DW used from
            3    IN1_OFST        uint8           0,4
                                                               operand 2
Operands
            4    IN2_gB_BASE     void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5    IN3_rI_OFFSET void *
                                                               base pointer
            6    IN3_PART        uint8           LOW,HIGH      Word part which is used for operand 5
            7    IN4_PM_PTR      void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rIp_pm_ptr (ndw_4dw, vIn, 0, ptrBase, ptrModify, LOW, ptr);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.

vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_pm_imm
name
Spec        vstdw {mdw [,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                          Determines the element size and number
                              MDW_options
            1    MDW
                              enum                        of stored elements (see enum definition
                                                          at vec-mem-modes.h)
            2    IN1_V32      vec_t                       Input vector operand
Operands    3
                                                          Offset for the first DW used from
                 IN1_OFST     uint8           0,4
                                                          operand 2
            4    IN2_PTR      void *                      Pointer register (rN)
                                                31   31   32 bit immediate post modification in
            5    IN3_IMM32_6 int32            -2 ..2 -1
                                                          bytes
            void* ptr;
            vec_t vIn;
C example   ...
            vstdw_v32_pm_imm (mdw_8dw, vIn, 0, ptr, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_pm_ptr
name

Spec        vstdw {mdw [,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                          Determines the element size and number
                              NDW_options
            1    NDW
                              enum                        of stored elements (see enum definition
                                                          at vec-mem-modes.h)
            2    IN1_V32      vec_t                       Input vector operand
Operands
                                                          Offset for the first DW used from
            3    IN1_OFST     uint8           0,4
                                                          operand 2
            4    IN2_PTR      void *                      Pointer register (rN)
            5    IN3_PM_PTR void*                         Pointer register (rN)
            void* ptr;
C example   vec_t vIn;
            ...
             vstdw_v32_pm_ptr (ndw_4dw, vIn, 0, ptr, ptr);

             1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                  vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                  some case, saturation might be wrongly applied if voX is allocated and DW
Comments          vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
             2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                  operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                  is applicable, bind the storted vec_t variable to a viX register (less
                  recommended).


Main table → Memory Access → Store → Store 32 bit double word
Available addressing modes
Intrinsic Names:
vstdw_v32_concat
vstdw_v32_direct_concat
vstdw_v32_indexed_imm_concat
vstdw_v32_indexed_rI_concat
vstdw_v32_indexed_rI_pm_imm_concat
vstdw_v32_indexed_rI_pm_ptr_concat
vstdw_v32_indexed_rIp_concat
vstdw_v32_indexed_rIp_pm_imm_concat
vstdw_v32_indexed_rIp_pm_ptr_concat
vstdw_v32_pm_imm_concat
vstdw_v32_pm_ptr_concat
Intrinsic   vstdw_v32_concat
name
Spec        vstdw {mdw [,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                          Determines the element size and number
                              MDW_options
            1    MDW

enum                        of stored elements (see enum definition at
                                                          vec-mem-modes.h)

Operands    2    IN1_V32      vec_t                       Input vector operand
                                                          Offset for the first DW used from
            3    IN1_OFST     uint8           0,4
                                                          operand 2
            4    IN2_PTR      void *                      Pointer register (rN)
            void* ptr;
            vec_t vIn;
C example   ...
            vstdw_v32_concat (mdw_8dw, vIn, 0, ptr);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_direct_concat
name
Spec        vstdw {mdw [,concat]} vix[0], [#address] [,?prSC]
syntax
Return      void
type
                                                          Determines the element size and number
                              MDW_options
            1    MDW
                              enum                        of stored elements (see enum definition at
                                                          vec-mem-modes.h)
Operands    2    IN1_V32      vec_t                       Input vector operand

            3    IN1_OFST     uint8
                                                          Offset for the first DW used from
                                              0,4
                                                          operand 2
                                                  32
            4    IN2_ADDR      int32          0..2 -1        32 bit address
            vec_t vIn;
C example   ...
            vstdw_v32_direct_concat (mdw_8dw, vIn, 0, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.

vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_imm_concat
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+#imm16_6) [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and
                                MDW_options
            1    MDW
                                enum                           number of stored elements (see enum
                                                               definition at vec-mem-modes.h)
            2    IN1_V32        vec_t                          Input vector operand
Operands                                                       Offset for the first DW used from
            3    IN1_OFST       uint8           0,4
                                                               operand 2
            4    IN2_gB_BASE void *                            Pointer register (gB)
                                                -              16 bit immediate post modification in
            5    IN3_IMM16_6    int16
                                                32768..32767   bytes
            void* ptrBase;
            vec_t vIn;
C example   ...
            vstdw_v32_indexed_imm_concat (mdw_8dw, vIn, 0, ptrBase, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).

Intrinsic   vstdw_v32_indexed_rI_concat
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2    IN1_V32         vec_t                         Input vector operand
Operands                                                       Offset for the first DW used from
            3    IN1_OFST        uint8            0,4
                                                               operand 2
            4    IN2_gB_BASE     void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                               the base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rI_concat (mdw_8dw, vIn, 0, ptrBase, ptrModify);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rI_pm_imm_concat
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                 MDW_options                   Determines the element size and number
Operands    1    MDW
                                 enum                          of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_V32         vec_t                        Input vector operand

3
                                                              Offset for the first DW used from
                 IN1_OFST        uint8           0,4
                                                              operand 2
            4    IN2_gB_BASE     void *                       Pointer register (gB)
                                                              Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                              the base pointer
                                                   31   31    32 bit immediate post modification in
            6    IN4_PM_IMM      int32           -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rI_pm_imm_concat (mdw_8dw, vIn, 0, ptrBase, ptrModify, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rI_pm_ptr_concat
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 NDW_options
            1    NDW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_V32         vec_t                        Input vector operand
Operands                                                      Offset for the first DW used from
            3    IN1_OFST        uint8           0,4
                                                              operand 2
            4    IN2_gB_BASE     void *                       Pointer register (gB)

5    IN3_rI_OFFSET void *
                                                              Pointer (rI) specifying the offset from the
                                                              base pointer
            6    IN4_PM_PTR      void*                          Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rI_pm_ptr_concat (ndw_4dw, vIn, 0, ptrBase, ptrModify, ptr);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rIp_concat
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2    IN1_V32         vec_t                          Input vector operand
                                                                Offset for the first DW used from
Operands    3    IN1_OFST        uint8            0,4
                                                                operand 2
            4    IN2_gB_BASE     void *                         Pointer register (gB)
                                                                Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                                the base pointer
            6    IN3_PART        uint8            LOW,HIGH      Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...

vstdw_v32_indexed_rIp_concat (mdw_8dw, vIn, 0, ptrBase, ptrModify, LOW);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
Comments         vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
            2.
                 some case, saturation might be wrongly applied if voX is allocated and DW
                 vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
                 VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_indexed_rIp_pm_imm_concat
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MDW_options
            1    MDW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_V32        vec_t                        Input vector operand
                                                             Offset for the first DW used from
            3    IN1_OFST       uint8           0,4
                                                             operand 2
Operands    4    IN2_gB_BASE    void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                             the base pointer
            6    IN3_PART       uint8           LOW,HIGH     Word part which is used for operand 5
                                                  31   31    32 bit immediate post modification in
            7    IN4_PM_IMM     int32           -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rIp_pm_imm_concat (mdw_8dw, vIn, 0, ptrBase, ptrModify, LOW, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.

vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).
Intrinsic   vstdw_v32_indexed_rIp_pm_ptr_concat
name
Spec        vstdw {mdw [,concat]} vix[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 NDW_options
            1    NDW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2    IN1_V32         vec_t                         Input vector operand
                                                               Offset for the first DW used from
            3    IN1_OFST        uint8           0,4
                                                               operand 2
Operands
            4    IN2_gB_BASE     void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            5    IN3_rI_OFFSET void *
                                                               base pointer
            6    IN3_PART        uint8           LOW,HIGH      Word part which is used for operand 5
            7    IN4_PM_PTR      void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec_t vIn;
            ...
            vstdw_v32_indexed_rIp_pm_ptr_concat (ndw_4dw, vIn, 0, ptrBase, ptrModify, LOW, ptr);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the

2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_pm_imm_concat
name
Spec        vstdw {mdw [,concat]} vix[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                              MDW_options
            1    MDW
                              enum                           of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_V32      vec_t                          Input vector operand
Operands    3
                                                             Offset for the first DW used from
                 IN1_OFST     uint8           0,4
                                                             operand 2
            4    IN2_PTR      void *                         Pointer register (rN)
                                                31   31      32 bit immediate post modification in
            5    IN3_IMM32_6 int32            -2 ..2 -1
                                                             bytes
            void* ptr;
            vec_t vIn;
C example   ...
            vstdw_v32_pm_imm_concat (mdw_8dw, vIn, 0, ptr, 2);

            1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                 vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                 some case, saturation might be wrongly applied if voX is allocated and DW
Comments         vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
            2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                 operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                 is applicable, bind the storted vec_t variable to a viX register (less
                 recommended).



Intrinsic   vstdw_v32_pm_ptr_concat
name
Spec        vstdw {mdw [,concat]} vix[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                              NDW_options

1    NDW
                              enum                           of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_V32      vec_t                          Input vector operand
Operands
                                                             Offset for the first DW used from
            3    IN1_OFST     uint8           0,4
                                                             operand 2
            4    IN2_PTR      void *                         Pointer register (rN)
            5    IN3_PM_PTR void*                            Pointer register (rN)
            void* ptr;
C example   vec_t vIn;
            ...
           vstdw_v32_pm_ptr_concat (ndw_4dw, vIn, 0, ptr, ptr);

           1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
                vstdw_v32 is not guaranteed to allocate a viX register when vec_t is used. In
                some case, saturation might be wrongly applied if voX is allocated and DW
Comments        vector saturation is enabled. To ensure DW saturation doesn't occur, disable the
           2.   VSATSDW mode bit (store saturation); or, use a vec40_t variable for the stored
                operand; or, for word data, use the vstw intrinsic; or, if non of the previous steps
                is applicable, bind the storted vec_t variable to a viX register (less
                recommended).


Main table → Memory Access → Store → Store 32 bit double word
Available addressing modes
Intrinsic Names:
vstdw_v40_indexed_rI_pm_imm_vuX
vstdw_v40_indexed_rI_pm_ptr_vuX
vstdw_v40_indexed_rI_vuX
vstdw_v40_indexed_rIp_pm_imm_vuX
vstdw_v40_indexed_rIp_pm_ptr_vuX
vstdw_v40_indexed_rIp_vuX
vstdw_v40_pm_imm_vuX
vstdw_v40_pm_ptr_vuX
vstdw_v40_vuX
Intrinsic   vstdw_v40_indexed_rI_pm_imm_vuX
name
Spec        vstdw {mdw, vuX } vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2    VUX             uint8           0..3         Determines the source VCU
            3    IN1_V40         vec40_t                      Output vector operand

Offset for the first DW used from
Operands    4    IN1_OFST        uint8           0,4
                                                              operand 3
            5    IN2_gB_BASE     void *                       Pointer register (gB)

            6
                                                              Pointer (rI) specifying the offset from
                 IN3_rI_OFFSET void *
                                                              the base pointer
                                                   31   31    32 bit immediate post modification in
            7    IN4_PM_IMM      int32           -2 ..2 -1
                                                              bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rI_pm_imm_vuX (mdw_8dw, 1, vIn, 0, ptrBase, ptrModify, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rI_pm_ptr_vuX
name
Spec        vstdw {mdw, vuX } vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                                 NDW_options
            1    NDW
                                 enum                         of stored elements (see enum definition
                                                              at vec-mem-modes.h)
Operands    2    VUX             uint8           0..3         Determines the source VCU
            3    IN1_V40         vec40_t                      Output vector operand
            4    IN1_OFST        uint8           0,4          Offset for the first DW used from
                                                                operand 3
            5    IN2_gB_BASE     void *                         Pointer register (gB)

            6
                                                                Pointer (rI) specifying the offset from the
                 IN3_rI_OFFSET void *
                                                                base pointer
            7    IN4_PM_PTR      void*                          Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rI_pm_ptr_vuX (ndw_4dw, 1, vIn, 0, ptrBase, ptrModify, ptr);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.

Intrinsic   vstdw_v40_indexed_rI_vuX
name
Spec        vstdw {mdw, vuX } vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2    VUX             uint8            0..3          Determines the source VCU
            3    IN1_V40         vec40_t                        Output vector operand
Operands
            4
                                                                Offset for the first DW used from
                 IN1_OFST        uint8            0,4
                                                                operand 3
            5    IN2_gB_BASE     void *                         Pointer register (gB)
                                                                Pointer (rI) specifying the offset from
            6    IN3_rI_OFFSET void *
                                                                the base pointer
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rI_vuX (mdw_8dw, 1, vIn, 0, ptrBase, ptrModify);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rIp_pm_imm_vuX
name
Spec        vstdw {mdw,vuX } vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MDW_options
            1    MDW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2    VUX            uint8           0..3         Determines the source VCU
            3    IN1_V40        vec40_t                      Output vector operand
                                                             Offset for the first DW used from
            4    IN1_OFST       uint8           0,4
Operands                                                     operand 3
            5    IN2_gB_BASE    void *                       Pointer register (gB)

Pointer (rI) specifying the offset from
            6    IN3_rI_OFFSET void *
                                                             the base pointer
            7    IN3_PART       uint8           LOW,HIGH     Word part which is used for operand 6
                                                  31   31    32 bit immediate post modification in
            8    IN4_PM_IMM     int32           -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rIp_pm_imm_vuX (mdw_8dw, 1, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rIp_pm_ptr_vuX
name
Spec        vstdw {mdw,vuX } vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                NDW_options
            1    NDW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)

Operands    2    VUX            uint8           0..3         Determines the source VCU
            3    IN1_V40        vec40_t                      Output vector operand

            4
                                                             Offset for the first DW used from
                 IN1_OFST       uint8           0,4
                                                             operand 3
            5    IN2_gB_BASE     void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from the
            6    IN3_rI_OFFSET void *
                                                               base pointer
            7    IN3_PART        uint8           LOW,HIGH      Word part which is used for operand 6
            8    IN4_PM_PTR      void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rIp_pm_ptr_vuX (ndw_4dw, 1, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rIp_vuX
name

Spec        vstdw {mdw,vuX } vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2    VUX             uint8           0..3          Determines the source VCU
            3    IN1_V40         vec40_t                       Output vector operand
Operands    4
                                                               Offset for the first DW used from
                 IN1_OFST        uint8           0,4
                                                               operand 3
            5    IN2_gB_BASE     void *                        Pointer register (gB)
                                                               Pointer (rI) specifying the offset from
            6    IN3_rI_OFFSET void *
                                                               the base pointer
            7    IN3_PART        uint8           LOW,HIGH      Word part which is used for operand 6
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rIp_vuX (mdw_8dw, 1, vIn, 0, ptrBase, ptrModify, LOW);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic    vstdw_v40_pm_imm_vuX
name
Spec        vstdw {mdw, vuX } vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                              MDW_options
            1    MDW
                              enum                          of stored elements (see enum definition at
                                                            vec-mem-modes.h)
            2    VUX          uint8           0..3          Determines the source VCU
            3    IN1_V40      vec40_t                       Output vector operand
Operands
                                                            Offset for the first DW used from
            4    IN1_OFST     uint8           0,4
                                                            operand 3
            5    IN2_PTR      void *                        Pointer register (rN)

31   31     32 bit immediate post modification in
            6    IN3_PM_IMM int32             -2 ..2 -1
                                                            bytes
            void* ptr;
            vec40_t vIn;
C example   ...
            vstdw_v40_pm_imm_vuX (mdw_8dw, 1, vIn, 0, ptr, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_pm_ptr_vuX
name
Spec        vstdw {mdw, vuX } vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                              NDW_options
            1    NDW
                              enum                          of stored elements (see enum definition
                                                            at vec-mem-modes.h)
            2    VUX          uint8           0..3          Determines the source VCU

Operands    3    IN1_V40      vec40_t                       Output vector operand
                                                            Offset for the first DW used from
            4    IN1_OFST     uint8           0,4
                                                            operand 3
            5    IN2_PTR      void *                        Pointer register (rN)
            6    IN3_PM_PTR void*                           Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstdw_v40_pm_ptr_vuX (ndw_4dw, 1, vIn, 0, ptr, ptr);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_vuX
name
Spec        vstdw {mdw, vuX } vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                              MDW_options
            1    MDW
                              enum                             of stored elements (see enum definition at
                                                               vec-mem-modes.h)
            2    VUX          uint8            0..3            Determines the source VCU
Operands    3    IN1_V40      vec40_t                          Output vector operand
                                                               Offset for the first DW used from
            4    IN1_OFST     uint8            0,4
                                                               operand 3

5    IN2_PTR      void *                           Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstdw_v40_vuX (mdw_8dw, 1, vIn, 0, ptr);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.


Main table → Memory Access → Store → Store 32 bit double word
Available addressing modes
Intrinsic Names:
vstdw_v40
vstdw_v40_direct
vstdw_v40_indexed_imm
vstdw_v40_indexed_rI
vstdw_v40_indexed_rI_pm_imm
vstdw_v40_indexed_rI_pm_ptr
vstdw_v40_indexed_rIp
vstdw_v40_indexed_rIp_pm_imm
vstdw_v40_indexed_rIp_pm_ptr
vstdw_v40_pm_imm
vstdw_v40_pm_ptr
Intrinsic   vstdw_v40
name
Spec        vstdw {mdw [,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                           Determines the element size and number
                              MDW_options
            1    MDW
                              enum                         of stored elements (see enum definition at
                                                           vec-mem-modes.h)

Operands    2    IN1_V40      vec40_t                      Output vector operand
                                                           Offset for the first DW used from
            3    IN1_OFST     uint8             0,4
                                                           operand 2
            4    IN2_PTR      void *                       Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstdw_v40 (mdw_8dw, vIn, 0, ptr);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_direct
name
Spec        vstdw {mdw [,concat]} vox[0], [#address] [,?prSC]
syntax
Return      void
type
                                                           Determines the element size and number
                              MDW_options
            1    MDW
                              enum                         of stored elements (see enum definition at
                                                           vec-mem-modes.h)

Operands    2    IN1_V40      vec40_t                      Output vector operand
                                                           Offset for the first DW used from
            3    IN1_OFST     uint8             0,4
                                                           operand 2
                                                      32

4    IN2_ADDR     int32             0..2 -1    32 bit address
            vec40_t vIn;
C example   ...
            vstdw_v40_direct (mdw_8dw, vIn, 0, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
Intrinsic   vstdw_v40_indexed_imm
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and
                                MDW_options
            1    MDW
                                enum                           number of stored elements (see enum
                                                               definition at vec-mem-modes.h)
            2    IN1_V40        vec40_t                        Output vector operand
Operands                                                       Offset for the first DW used from
            3    IN1_OFST       uint8           0,4
                                                               operand 2
            4    IN2_gB_BASE void *                            Pointer register (gB)
                                                -              16 bit immediate post modification in
            5    IN3_IMM16_6    int16
                                                32768..32767   bytes
            void* ptrBase;
            vec40_t vIn;
C example   ...
            vstdw_v40_indexed_imm (mdw_8dw, vIn, 0, ptrBase, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rI
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                MDW_options
            1    MDW
                                enum                           of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2    IN1_V40        vec40_t                        Output vector operand
Operands                                                       Offset for the first DW used from
            3    IN1_OFST       uint8            0,4
                                                               operand 2
            4    IN2_gB_BASE    void *                         Pointer register (gB)

Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                               the base pointer
C example   void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
            ...
            vstdw_v40_indexed_rI (mdw_8dw, vIn, 0, ptrBase, ptrModify);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rI_pm_imm
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2    IN1_V40         vec40_t                        Output vector operand
                                                                Offset for the first DW used from
            3    IN1_OFST        uint8            0,4
Operands                                                        operand 2
            4    IN2_gB_BASE     void *                         Pointer register (gB)

            5
                                                                Pointer (rI) specifying the offset from
                 IN3_rI_OFFSET void *
                                                                the base pointer
                                                    31   31     32 bit immediate post modification in
            6    IN4_PM_IMM      int32            -2 ..2 -1
                                                                bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rI_pm_imm (mdw_8dw, vIn, 0, ptrBase, ptrModify, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rI_pm_ptr
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                 NDW_options                    Determines the element size and number
Operands    1    NDW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)

2    IN1_V40         vec40_t                        Output vector operand

            3
                                                                Offset for the first DW used from
                 IN1_OFST        uint8            0,4
                                                                operand 2
            4    IN2_gB_BASE     void *                         Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5    IN3_rI_OFFSET void *
                                                                base pointer
            6    IN4_PM_PTR      void*                          Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rI_pm_ptr (ndw_4dw, vIn, 0, ptrBase, ptrModify, ptr);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rIp
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2    IN1_V40         vec40_t                        Output vector operand
                                                                Offset for the first DW used from
            3    IN1_OFST        uint8            0,4
Operands                                                        operand 2
            4    IN2_gB_BASE     void *                         Pointer register (gB)
                                                                Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                                the base pointer
            6    IN3_PART        uint8            LOW,HIGH      Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rIp (mdw_8dw, vIn, 0, ptrBase, ptrModify, LOW);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
Intrinsic   vstdw_v40_indexed_rIp_pm_imm

name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MDW_options
            1    MDW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_V40        vec40_t                      Output vector operand
                                                             Offset for the first DW used from
            3    IN1_OFST       uint8           0,4
                                                             operand 2
Operands    4    IN2_gB_BASE    void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                             the base pointer
            6    IN3_PART       uint8           LOW,HIGH     Word part which is used for operand 5
                                                  31   31    32 bit immediate post modification in
            7    IN4_PM_IMM     int32           -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rIp_pm_imm (mdw_8dw, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rIp_pm_ptr
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                NDW_options
            1    NDW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
Operands
            2    IN1_V40        vec40_t                      Output vector operand
            3    IN1_OFST       uint8           0,4          Offset for the first DW used from
                                                               operand 2
            4    IN2_gB_BASE     void *                        Pointer register (gB)

            5

Pointer (rI) specifying the offset from the
                 IN3_rI_OFFSET void *
                                                               base pointer
            6    IN3_PART        uint8           LOW,HIGH      Word part which is used for operand 5
            7    IN4_PM_PTR      void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rIp_pm_ptr (ndw_4dw, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_pm_imm
name
Spec        vstdw {mdw [,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                               MDW_options
            1    MDW
                               enum                           of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_V40       vec40_t                        Output vector operand
Operands    3
                                                              Offset for the first DW used from
                 IN1_OFST      uint8            0,4
                                                              operand 2
            4    IN2_PTR       void *                         Pointer register (rN)
                                                  31   31     32 bit immediate post modification in
            5    IN3_IMM32_6 int32              -2 ..2 -1
                                                              bytes
            void* ptr;
            vec40_t vIn;
C example   ...
            vstdw_v40_pm_imm (mdw_8dw, vIn, 0, ptr, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_pm_ptr
name
Spec         vstdw {mdw [,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return       void
type
                                                             Determines the element size and number
                                NDW_options
             1    NDW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
             2    IN1_V40       vec40_t                      Output vector operand

Operands
                                                             Offset for the first DW used from
             3    IN1_OFST      uint8            0,4
                                                             operand 2
             4    IN2_PTR       void *                       Pointer register (rN)
             5    IN3_PM_PTR void*                           Pointer register (rN)
             void* ptr;
             vec40_t vIn;
C example    ...
             vstdw_v40_pm_ptr (ndw_4dw, vIn, 0, ptr, ptr);

Comments     1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.


Main table → Memory Access → Store → Store 32 bit double word
Available addressing modes
Intrinsic Names:
vstdw_v40_concat
vstdw_v40_direct_concat
vstdw_v40_indexed_imm_concat
vstdw_v40_indexed_rI_concat
vstdw_v40_indexed_rI_pm_imm_concat
vstdw_v40_indexed_rI_pm_ptr_concat
vstdw_v40_indexed_rIp_concat
vstdw_v40_indexed_rIp_pm_imm_concat
vstdw_v40_indexed_rIp_pm_ptr_concat
vstdw_v40_pm_imm_concat
vstdw_v40_pm_ptr_concat
Intrinsic   vstdw_v40_concat
name
Spec        vstdw {mdw [,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                              MDW_options
            1    MDW
                              enum                          of stored elements (see enum definition at
                                                            vec-mem-modes.h)

Operands    2    IN1_V40      vec40_t                       Output vector operand
                                                            Offset for the first DW used from
            3    IN1_OFST     uint8           0,4
                                                            operand 2
            4    IN2_PTR      void *                        Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstdw_v40_concat (mdw_8dw, vIn, 0, ptr);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_direct_concat
name
Spec        vstdw {mdw [,concat]} vox[0], [#address] [,?prSC]
syntax
Return      void
type
                                                            Determines the element size and number
                              MDW_options
            1    MDW
                              enum                          of stored elements (see enum definition at

vec-mem-modes.h)

Operands    2    IN1_V40      vec40_t                       Output vector operand
                                                            Offset for the first DW used from
            3    IN1_OFST     uint8           0,4
                                                            operand 2
                                                    32
            4    IN2_ADDR     int32           0..2 -1       32 bit address
            vec40_t vIn;
C example   ...
            vstdw_v40_direct_concat (mdw_8dw, vIn, 0, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
Intrinsic   vstdw_v40_indexed_imm_concat
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+#imm16_6) [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and
                                MDW_options
            1    MDW
                                enum                           number of stored elements (see enum
                                                               definition at vec-mem-modes.h)
            2    IN1_V40        vec40_t                        Output vector operand
Operands                                                       Offset for the first DW used from
            3    IN1_OFST       uint8           0,4
                                                               operand 2
            4    IN2_gB_BASE void *                            Pointer register (gB)
                                                -              16 bit immediate post modification in
            5    IN3_IMM16_6    int16
                                                32768..32767   bytes
            void* ptrBase;
            vec40_t vIn;
C example   ...
            vstdw_v40_indexed_imm_concat (mdw_8dw, vIn, 0, ptrBase, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rI_concat
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                MDW_options
            1    MDW
                                enum                           of stored elements (see enum definition
                                                               at vec-mem-modes.h)

2    IN1_V40        vec40_t                        Output vector operand
Operands                                                       Offset for the first DW used from
            3    IN1_OFST       uint8            0,4
                                                               operand 2
            4    IN2_gB_BASE    void *                         Pointer register (gB)
                                                               Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                               the base pointer
C example   void* ptrBase;
            void* ptrModify;
            vec40_t vIn;
            ...
            vstdw_v40_indexed_rI_concat (mdw_8dw, vIn, 0, ptrBase, ptrModify);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rI_pm_imm_concat
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                          of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2    IN1_V40         vec40_t                       Output vector operand
                                                               Offset for the first DW used from
            3    IN1_OFST        uint8            0,4
Operands                                                       operand 2
            4    IN2_gB_BASE     void *                        Pointer register (gB)

            5
                                                               Pointer (rI) specifying the offset from
                 IN3_rI_OFFSET void *
                                                               the base pointer
                                                    31   31    32 bit immediate post modification in
            6    IN4_PM_IMM      int32            -2 ..2 -1
                                                               bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rI_pm_imm_concat (mdw_8dw, vIn, 0, ptrBase, ptrModify, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.

Intrinsic   vstdw_v40_indexed_rI_pm_ptr_concat
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rI)[+pm] [,?prSC]
syntax
Return      void
type
                                 NDW_options                   Determines the element size and number
Operands    1    NDW
                                 enum                          of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2    IN1_V40         vec40_t                        Output vector operand

            3
                                                                Offset for the first DW used from
                 IN1_OFST        uint8            0,4
                                                                operand 2
            4    IN2_gB_BASE     void *                         Pointer register (gB)
                                                                Pointer (rI) specifying the offset from the
            5    IN3_rI_OFFSET void *
                                                                base pointer
            6    IN4_PM_PTR      void*                          Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rI_pm_ptr_concat (ndw_4dw, vIn, 0, ptrBase, ptrModify, ptr);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rIp_concat
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                                Determines the element size and number
                                 MDW_options
            1    MDW
                                 enum                           of stored elements (see enum definition
                                                                at vec-mem-modes.h)
            2    IN1_V40         vec40_t                        Output vector operand
                                                                Offset for the first DW used from
            3    IN1_OFST        uint8            0,4
Operands                                                        operand 2
            4    IN2_gB_BASE     void *                         Pointer register (gB)
                                                                Pointer (rI) specifying the offset from

5    IN3_rI_OFFSET void *
                                                                the base pointer
            6    IN3_PART        uint8            LOW,HIGH      Word part which is used for operand 5
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rIp_concat (mdw_8dw, vIn, 0, ptrBase, ptrModify, LOW);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.
Intrinsic   vstdw_v40_indexed_rIp_pm_imm_concat
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                MDW_options
            1    MDW
                                enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
            2    IN1_V40        vec40_t                      Output vector operand
                                                             Offset for the first DW used from
            3    IN1_OFST       uint8           0,4
                                                             operand 2
Operands    4    IN2_gB_BASE    void *                       Pointer register (gB)
                                                             Pointer (rI) specifying the offset from
            5    IN3_rI_OFFSET void *
                                                             the base pointer
            6    IN3_PART       uint8           LOW,HIGH     Word part which is used for operand 5
                                                  31   31    32 bit immediate post modification in
            7    IN4_PM_IMM     int32           -2 ..2 -1
                                                             bytes
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rIp_pm_imm_concat (mdw_8dw, vIn, 0, ptrBase, ptrModify, LOW, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_indexed_rIp_pm_ptr_concat
name
Spec        vstdw {mdw [,concat]} vox[0], (gB+rIp)[+pm] [,?prSC]
syntax
Return      void
type
                                                             Determines the element size and number
                                NDW_options
            1    NDW

enum                         of stored elements (see enum definition
                                                             at vec-mem-modes.h)
Operands
            2    IN1_V40        vec40_t                      Output vector operand
            3    IN1_OFST       uint8           0,4          Offset for the first DW used from
                                                               operand 2
            4    IN2_gB_BASE     void *                        Pointer register (gB)

            5
                                                               Pointer (rI) specifying the offset from the
                 IN3_rI_OFFSET void *
                                                               base pointer
            6    IN3_PART        uint8           LOW,HIGH      Word part which is used for operand 5
            7    IN4_PM_PTR      void*                         Pointer register (rN)
            void* ptr;
            void* ptrBase;
            void* ptrModify;
C example   vec40_t vIn;
            ...
            vstdw_v40_indexed_rIp_pm_ptr_concat (ndw_4dw, vIn, 0, ptrBase, ptrModify, LOW, ptr);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_pm_imm_concat
name
Spec        vstdw {mdw [,concat]} vox[0], (pN)+#imm32_6 [,?prSC]
syntax
Return      void
type
                                                              Determines the element size and number
                               MDW_options
            1    MDW
                               enum                           of stored elements (see enum definition
                                                              at vec-mem-modes.h)
            2    IN1_V40       vec40_t                        Output vector operand
Operands    3
                                                              Offset for the first DW used from
                 IN1_OFST      uint8            0,4
                                                              operand 2
            4    IN2_PTR       void *                         Pointer register (rN)
                                                  31   31     32 bit immediate post modification in
            5    IN3_IMM32_6 int32              -2 ..2 -1
                                                              bytes
            void* ptr;
            vec40_t vIn;
C example   ...
            vstdw_v40_pm_imm_concat (mdw_8dw, vIn, 0, ptr, 2);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.



Intrinsic   vstdw_v40_pm_ptr_concat
name
Spec        vstdw {mdw [,concat]} vox[0], (pN)[+pm_x] [,?prSC]
syntax
Return      void
type
                                                               Determines the element size and number
                               NDW_options
            1    NDW
                               enum                            of stored elements (see enum definition
                                                               at vec-mem-modes.h)
            2    IN1_V40       vec40_t                         Output vector operand
Operands
                                                               Offset for the first DW used from
            3    IN1_OFST      uint8            0,4
                                                               operand 2
            4    IN2_PTR       void *                          Pointer register (rN)
            5    IN3_PM_PTR void*                              Pointer register (rN)
            void* ptr;
            vec40_t vIn;
C example   ...
            vstdw_v40_pm_ptr_concat (ndw_4dw, vIn, 0, ptr, ptr);

Comments    1.   If IN1_OFST equals 4, then MDW must be in the range 1-4.


Main table → Memory Access → Store → Store 32 bit double word
Available addressing modes
Intrinsic Names:
vstdw_v40ext_2dw_vuX
vstdw_v40ext_indexed_rI_2dw_vuX
vstdw_v40ext_indexed_rI_pm_imm_2dw_vuX
vstdw_v40ext_indexed_rI_pm_ptr_2dw_vuX
vstdw_v40ext_indexed_rIp_2dw_vuX
vstdw_v40ext_indexed_rIp_pm_imm_2dw_vuX
vstdw_v40ext_indexed_rIp_pm_ptr_2dw_vuX
vstdw_v40ext_pm_imm_2dw_vuX
vstdw_v40ext_pm_ptr_2dw_vuX
Intrinsic     vstdw_v40ext_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX           uint8      0..3           Determines the source VCU
Operands      2      IN1_V40       vec40_t                   Output vector operand
              3      IN2_PTR       void *                    Pointer register (rN)
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_2dw_vuX (1, vIn, ptr);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   VUX               uint8      0..3           Determines the source VCU
              2   IN1_V40           vec40_t                   Output vector operand

Operands      3   IN2_gB_BASE       void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                              base pointer
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_2dw_vuX (1, vIn, ptrBase, ptrModify);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_imm_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   VUX               uint8      0..3           Determines the source VCU
Operands
              2   IN1_V40           vec40_t                   Output vector operand
              3   IN2_gB_BASE       void *                    Pointer register (gB)
                                                              Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                              base pointer

              5                                 31   31       32 bit immediate post modification in
                  IN4_PM_IMM        int32     -2 ..2 -1
                                                              bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_imm_2dw_vuX (1, vIn, ptrBase, ptrModify, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_rI_pm_ptr_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rI)[+pm] [,?prSC]

Return type   void

              1   VUX               uint8     0..3            Determines the source VCU
              2   IN1_V40           vec40_t                   Output vector operand
              3   IN2_gB_BASE       void *                    Pointer register (gB)
Operands
                                                              Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                              base pointer
              5   IN4_PM_PTR        void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rI_pm_ptr_2dw_vuX (1, vIn, ptrBase, ptrModify, ptr);

Comments

Intrinsic     vstdw_v40ext_indexed_rIp_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   VUX               uint8     0..3            Determines the source VCU
Operands      2   IN1_V40           vec40_t                   Output vector operand
              3   IN2_gB_BASE       void *                    Pointer register (gB)
                                                             Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                             base pointer
              5   IN3_PART          uint8     LOW,HIGH       Word part which is used for operand 4
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_2dw_vuX (1, vIn, ptrBase, ptrModify, LOW);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_pm_imm_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   VUX               uint8     0..3           Determines the source VCU
              2   IN1_V40           vec40_t                  Output vector operand
              3   IN2_gB_BASE       void *                   Pointer register (gB)

Operands                                                     Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                             base pointer
              5   IN3_PART          uint8     LOW,HIGH       Word part which is used for operand 4
                                                31   31      32 bit immediate post modification in
              6   IN4_PM_IMM        int32     -2 ..2 -1
                                                             bytes
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_imm_2dw_vuX (1, vIn, ptrBase, ptrModify, LOW, 2);

Comments



Intrinsic     vstdw_v40ext_indexed_rIp_pm_ptr_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (gB+rIp)[+pm] [,?prSC]

Return type   void

              1   VUX               uint8     0..3           Determines the source VCU
Operands      2   IN1_V40           vec40_t                  Output vector operand
              3   IN2_gB_BASE       void *                   Pointer register (gB)

Pointer (rI) specifying the offset from the
              4   IN3_rI_OFFSET void *
                                                              base pointer
              5   IN3_PART          uint8    LOW,HIGH         Word part which is used for operand 4
              6   IN4_PM_PTR        void*                     Pointer register (rN)
              void* ptr;
              void* ptrBase;
              void* ptrModify;
C example     vec40_t vIn;
              ...
              vstdw_v40ext_indexed_rIp_pm_ptr_2dw_vuX (1, vIn, ptrBase, ptrModify, LOW, ptr);

Comments



Intrinsic     vstdw_v40ext_pm_imm_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX          uint8     0..3              Determines the source VCU
              2      IN1_V40      vec40_t                     Output vector operand
Operands      3      IN2_PTR      void *                      Pointer register (rN)
                                              31   31         32 bit immediate post modification in
              4      IN3_PM_IMM int32       -2 ..2 -1
                                                              bytes
              void* ptr;
              vec40_t vIn;
C example     ...
              vstdw_v40ext_pm_imm_2dw_vuX (1, vIn, ptr, 2);

Comments



Intrinsic     vstdw_v40ext_pm_ptr_2dw_vuX
name
Spec syntax   vstdw {2dw, vuX} vox[0]e, (pN)[+pm_x] [,?prSC]

Return type   void

              1      VUX          uint8     0..3              Determines the source VCU
              2      IN1_V40      vec40_t                     Output vector operand
Operands
              3      IN2_PTR      void *                      Pointer register (rN)
              4      IN3_PM_PTR void*                         Pointer register (rN)
C example     void* ptr;
            vec40_t vIn;
            ...
            vstdw_v40ext_pm_ptr_2dw_vuX (1, vIn, ptr, ptr);

Comments


Main table → Memory Access → Store → Store 32 bit double word
