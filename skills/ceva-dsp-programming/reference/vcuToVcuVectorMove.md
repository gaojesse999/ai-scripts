# Move And Pack → VCU to VCU Move → VCU to VCU Vector Move

*Auto-generated from CEVA-XC4500 Vec-C Intrinsics documentation*

---

Main table → Move And Pack → VCU to VCU Move → VCU to VCU Vector Move

VCU to VCU Vector Move

VCU to VCU Vector Move
Performs move between two VCUs. The sources is 40-bit wide and the destination is either 32-
bit or 40-bit wide determined by the vector register type.
Available Switches
vuX           Determines the VCU of the vox and voz registers.
Intrinsic Names
vvmov_v40_v32_vuX
Instruction details in the instruction set specification
Intrinsic     vvmov_v40_v32_vuX[_p]
name
Spec syntax   vvmov {vuX} vox[0], vz[0], ?vprX

Return type   vec_t

              1    VUX            uint8     0..3              Determines the source VCU
Operands      2    IN1_V40        vec40_t                     Output vector operand
              3    IN_VPR         vprex_t                     Vector predicate operand
              vec40_t vIn;
              vec_t vRes;
C example     vprex_t vecPred;
              ...
              vRes = vvmov_v40_v32_vuX_p (1, vIn, vecPred);

Comments      1.   IN_VPR last operand is relevant only for vvmov_v40_v32_vuX_p version.


Main table → Move And Pack → VCU to VCU Move → VCU to VCU Vector Move
