# CEVA DSP Intrinsics Summary

This document provides a comprehensive list of CEVA DSP intrinsics used in the l1sw project under `app/dsp` directory.

## Table of Contents
- [Overview](#overview)
- [Vector Load Operations](#vector-load-operations)
- [Vector Store Operations](#vector-store-operations)
- [Vector Arithmetic Operations](#vector-arithmetic-operations)
- [Vector Multiply Operations](#vector-multiply-operations)
- [Vector Shift Operations](#vector-shift-operations)
- [Vector Comparison Operations](#vector-comparison-operations)
- [Vector Logical Operations](#vector-logical-operations)
- [Vector Pack/Unpack Operations](#vector-packunpack-operations)
- [Vector Clear and Fill Operations](#vector-clear-and-fill-operations)
- [Vector Special Operations](#vector-special-operations)
- [Bit Field Configuration Operations](#bit-field-configuration-operations)
- [Mode Register Operations](#mode-register-operations)
- [Floating Point Operations](#floating-point-operations)

---

## Overview

CEVA DSP intrinsics are low-level functions that map directly to DSP assembly instructions. They provide fine-grained control over vector operations, memory access patterns, and hardware configuration for optimal signal processing performance.

### Common Naming Conventions

- **`_v`** prefix: Vector operations
- **`_l`** prefix: Load operations
- **`_s`** prefix: Store operations
- **`mdw_Xdw`**: Multi-double-word (e.g., `mdw_8dw` = 8 double-words = 32 bytes)
- **`_declaration`**: Declares temporary variables for the intrinsic
- **`_p`**: Predicated execution (conditional based on VPR register)
- **`_s`**: Saturating arithmetic
- **`_vuX`**: Vector unit selection (VCU0, VCU1)
- **`_const`**: Constant operand mode

---

## Vector Load Operations

### Basic Vector Load

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vlddw_v32(mdw, src, dest, offset)` | Load 32-bit vector from memory | `_vlddw_v32(mdw_8dw, input, vIn, 0)` |
| `_vlddw_v40(mdw, src, dest, offset)` | Load 40-bit vector from memory | `_vlddw_v40(mdw_8dw, data, vOut, 0)` |
| `_vlddw_c32_1dw(src, dest)` | Load single 32-bit scalar | `_vlddw_c32_1dw(l_prbs_bits, l_tmp)` |
| `_vlddw_c32_clone_1dw(src, dest)` | Load and replicate scalar | `_vlddw_c32_clone_1dw(&scale, vcScale)` |
| `_vlddw_c32_clone_2dw(src, dest1, dest2)` | Load 2 scalars | `_vlddw_c32_clone_2dw(inParams->kPrime, cKPrime0, cKPrime1)` |

### Vector Load with Post-Modification

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vlddw_pm_imm_v32(mdw, src, dest, step, offset)` | Load with immediate post-modify | `_vlddw_pm_imm_v32(mdw_8dw, phs, vphs, step16dwInBytes, 0)` |
| `_vlddw_pm_imm_vpr_dw(src, vpr, step)` | Load VPR with post-modify | `_vlddw_pm_imm_vpr_dw(prbsBegin, vpr0Seq, 8)` |

### Vector Load with Vector Unit Selection

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vlddw_v32_vuX(mdw, vcu, src, dest, offset)` | Load to specific VCU | `_vlddw_v32_vuX(mdw_1dw, VCU0, in32, vin, 0)` |
| `_vlddw_v40_vuX(mdw, vcu, src, dest, offset)` | Load 40-bit to VCU | `_vlddw_v40_vuX(mdw_8dw, VCU1, data, vOut, 0)` |

### Vector Load Clone

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vlddw_v32_clone(mdw, src, dest, offset)` | Load and replicate across vector | `_vlddw_v32_clone(mdw_8dw, cfg, viCfg, 0)` |

### Vector Load VPR (Vector Predicate Register)

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vlddw_vpr_dw(src, dest)` | Load vector predicate register | `_vlddw_vpr_dw(&vcuSeq, vpr0Seq)` |

**Files:** `CalculateCorrShortAntDmrs.cpp`, `GenerateDmrs.cpp`, `ScaleCQ.cpp`, `RimRsMapperAlg.cpp`, `CsiRsMapperAlg.cpp`

---

## Vector Store Operations

### Basic Vector Store

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vstdw_v32(mdw, src, offset, dest)` | Store 32-bit vector | `_vstdw_v32(mdw_8dw, vOut, 0, output)` |
| `_vstdw_v40(mdw, src, offset, dest)` | Store 40-bit vector | `_vstdw_v40(mdw_8dw, vo0, 0, data)` |
| `_vstdw_v32_concat(mdw, src, offset, dest)` | Store concatenated vector | `_vstdw_v32_concat(mdw_4dw, vOut, 0, tmp)` |
| `_vstdw_c32_dw_concat(src, dest)` | Store scalar concatenated | `_vstdw_c32_dw_concat(vc0, dataPtr)` |

### Vector Store with Post-Modification

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vstdw_v32_pm_imm(mdw, src, offset, dest, step)` | Store with post-modify | `_vstdw_v32_pm_imm(mdw_8dw, vSeq, 0, outSeq, pmStep)` |

### Vector Store with Vector Unit Selection

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vstdw_v32_vuX(mdw, vcu, src, offset, dest)` | Store from specific VCU | `_vstdw_v32_vuX(mdw_8dw, VCU0, vOut, 0, output)` |
| `_vstdw_v40_vuX(mdw, vcu, src, offset, dest)` | Store 40-bit from VCU | `_vstdw_v40_vuX(mdw_2dw, VCU0, viRes, 0, corrShortAnt)` |

### Vector Store Word

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vstw_v32_hp_concat(mw, src, dest)` | Store half-precision word | `_vstw_v32_hp_concat(mw_8w, vOut, out)` |
| `_vstw_v32_lp(mw, src, dest)` | Store low-precision word | `_vstw_v32_lp(mw_8w, ofdmV, ofdmSeq)` |
| `_vstw_v40_v40_hp(pw, src1, src2, dest)` | Store two 40-bit vectors | `_vstw_v40_v40_hp(pw_16w, vOut0, vOut1, output)` |

**Files:** `CalculateCorrShortAntDmrs.cpp`, `VecFlp2Int.cpp`, `ScaleCQ.cpp`, `NrDlJob.cpp`

---

## Vector Arithmetic Operations

### Addition

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vadd32_v32_v32_v32(oop, va, vb, vout)` | 32-bit vector add | `_vsub32_v32_v32_v32(mdw_8dw, vExp, vFlpShift, vExp)` |
| `_vadd32_v32_c32_v32(oop, vin, c, vout)` | Vector add with scalar | `_vadd32_v32_c32_v32(8, vKlBar, cK0, vKlBar)` |
| `_vadd16_v32_c32_v32(oop, vin, c, low/high, vout)` | 16-bit add with scalar | `_vadd16_v32_c32_v32(oop_8op, viNeqMsb, vcThirtyOne, LOW, vShift)` |
| `_vadd40_v40_v40_v40(oop, va, vb, vout)` | 40-bit vector add | `_vadd40_v40_v40_v40_out(mdw_2dw, viRes, viRes1, viRes)` |
| `_vadd64_v32_v32_v32(mdw, va, vb, vout)` | 64-bit add (for accumulation) | `_vadd64_v32_v32_v32(mdw_4dw, viSum, viSum0, viSum)` |

### Integer Addition with Cross-Lane

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vaddint_v32_v32(oop, vin, vout)` | Integer horizontal add | `_vaddint_v32_v32(OOP, IN1, outZ)` |
| `_vaddint_v32_v40(oop, vin, vout)` | Integer add to 40-bit | `_vaddint_v32_v40(OOP, inA, outZ)` |
| `_vaddintx_v32_v40_3p(oop, vin, vout, offset)` | Extended integer add | `_vaddintx_v32_v40_3p(mdw_2dw, viRes, viRes, 0)` |

### Subtraction

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vsub32_v32_v32_v32(oop, va, vb, vout)` | 32-bit vector subtract | `_vsub32_v32_v32_v32(8, vExp, vFlpShift, vExp)` |
| `_vsub16_v32_v32_v32(oop, va, vb, vout)` | 16-bit vector subtract | `_vsub16_v32_v32_v32(oop_8op, v32, vBit, vNoiseBitsW)` |
| `_vsub16_v32_c32_v32(oop, vin, c, low/high, vout)` | 16-bit subtract with scalar | `_vsub16_v32_c32_v32(oop_8op, vMsb, vcSixteen, LOW, vLayer0)` |

### Negation

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vnegw_v32_v32(oop, vin, vout)` | Negate 32-bit vector | `_vnegw_v32_v32(8, vi0CoefPlus, vi1CoefMinus)` |

**Files:** `CalculateCorrShortAntDmrs.cpp`, `LogarithmMacros.hpp`, `UpdateNoiseNlExp.hpp`, `CsiRsMapperAlg.cpp`

---

## Vector Multiply Operations

### Basic Multiplication

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vmpyll_v32_c32_v32(mdw, vin, offset, c, vout)` | Low-low multiply | `_vmpyll_v32_c32_v32(mdw_4dw, viRes, 0, vcInvNoisePower, viRes)` |
| `_vmpywlxr_v32_v32_v32_SHFL16(oop, va, offa, vb, offb, vout)` | Word multiply with shuffle | `_vmpywlxr_v32_v32_v32_SHFL16(4, b_ssV, 0, ssV, 0, ofdmV)` |

### Complex Multiplication

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vmpyxp_v32_v32_v32(oop, va, offa, vb, offb, vout)` | Complex multiply preserving | `_vmpyxp_v32_v32_v32(8, viModSeq, 0, viScaledPhaseComp, 0, viScaledCompSeq)` |
| `_vmpyxrp_v32_c32_v32(oop, vin, offset, c, low/high, vout)` | Complex multiply with scalar | `_vmpyxrp_v32_c32_v32(8, viPhaseComp, 0, vcTxScaler, LOW, viScaledPhaseComp)` |
| `_vmpyxp_v32_c32_v32(oop, vin, offset, c, vout)` | Complex multiply preserving | `_vmpyxp_v32_c32_v32(5, vTaps0, 0, cRot, vTaps0)` |
| `_vmpyx_v32_v32_v32_v32_const_vmpsX(oop, vmps, va, offa, vb, offb, vout0, vout1)` | Complex multiply with VPS | `_vmpyx_v32_v32_v32_v32_const_vmpsX(8, VMPS1, vIn, 0, vTaps0, 0, vOut0, vOut1)` |

### Multiply-Accumulate (MAC)

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vmacx_v32_v32_v40_v40_const_vmpsX(oop, vmps, va, offa, vb, offb, vacc0, vout0, vout1)` | Complex MAC with VPS | `_vmacx_v32_v32_v40_v40_const_vmpsX(8, VMPS1, vIn, 0, vTaps0, 1, vOut0, vOut0, vOut1)` |
| `_vmsulw_v32_c32_v40_SHFL16(oop, vin, offset, c, low/high, vacc, vout)` | Multiply-subtract word | `_vmsulw_v32_c32_v40_SHFL16(8, xV, 0, cV, LOW, pssVec, pssVec)` |

### Special Multiply

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vgenmac3_v32_v32_v40(mdw, vcfg, va, vb, vacc, vout)` | General MAC 3-operand | `_vgenmac3_v32_v32_v40(mdw_6dw, viCfg, viIn0, viIn1, voMult, voMult)` |

**Files:** `CalculateCorrShortAntDmrs.cpp`, `MapSsAlg.cpp`, `GeneratePssAlg.cpp`, `FrequencyOffsetIntraSymbolAlgMultiUe.hpp`

---

## Vector Shift Operations

### Logical Shift

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vshiftl_v32_c32_v32(mdw, vin, c, vout)` | Vector shift left | `_vshiftl_v32_c32_v32(mdw_4dw, viSum, vcTmp1, viSum)` |
| `_vshift_v32_imm6_v32(oop, vin, imm, vout)` | Shift by immediate | `_vshift_v32_imm6_v32(8, vExp, -23, vExp)` |
| `_vshift_v32_imm6_v32_lg(oop, vin, imm, vout)` | Logical shift immediate | `_vshift_v32_imm6_v32_lg(8, vKAddCoef, -8, vKAddCoef)` |
| `_vshift_v32_v32_v32_w_lg(oop, vin, vsh, offset, vout)` | Logical shift by vector | `_vshift_v32_v32_v32_w_lg(oop_8op, viOne, vShift, 0, vMsbMask)` |

### Arithmetic Shift

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vshift_v32_c32p_v32_ar(mdw, vin, c, low/high, vout)` | Arithmetic shift with scalar | `_vshift_v32_c32p_v32_ar(mdw_8dw, vOut, leftShift, LOW, vOut)` |
| `_vshiftwx_v32_v32_v32_w_ar(oop, vin, vsh, offset, vout)` | Word arithmetic shift | `_vshiftwx_v32_v32_v32_w_ar(8, vIn, vScale, 0, vIn)` |

**Files:** `CalculateCorrShortAntDmrs.cpp`, `VecFlp2Int.cpp`, `LogarithmMacros.hpp`, `CsiRsMapperAlg.cpp`, `FrequencyOffsetIntraSymbolAlgMultiUe.hpp`

---

## Vector Comparison Operations

### Comparison with Predicate Result

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vcmpw_v32_v32_vpr_eq(oop, va, vb, vpr)` | Compare equal, result in VPR | `_vcmpw_v32_v32_vpr_eq(8, l_v_tmp, l_v_shift, l_prex_mov)` |
| `_vcmpw_v32_imm16_6_vpr_ge(oop, vin, imm, vpr)` | Compare >= immediate | `_vcmpw_v32_imm16_6_vpr_ge(oop_8op, vLayer0, 8, pMapToZero)` |
| `_vcmpw_v32_imm16_6_vpr_lt(oop, vin, imm, vpr)` | Compare < immediate | `_vcmpw_v32_imm16_6_vpr_lt(8, vData, threshold, vpr)` |

### Other Comparison

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vcmp20_v40_c32_vpr(oop, vin, c, vpr)` | 20-bit compare | `_vcmp20_v40_c32_vpr(OOP, inA, c, vpr)` |

**Files:** `GeneratePbchDmRs.cpp`, `LogicalAntennaPortUtilsVect.hpp`

---

## Vector Logical Operations

### Bitwise Operations

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vand_v32_v32_v32(oop, va, vb, vout)` | Vector AND | `_vand_v32_v32_v32(8, l_v_bits, l_v_shift, l_v_tmp)` |
| `_vandnot_v32_v32_v32(oop, va, vb, vout)` | Vector AND NOT | `_vandnot_v32_v32_v32(8, vA, vB, vOut)` |
| `_vor_v32_v32_v32(oop, va, vb, vout)` | Vector OR | `_vor_v32_v32_v32(8, vA, vB, vOut)` |
| `_vxor_v40_v40_v32(oop, va, vb, vout)` | Vector XOR | `_vxor_v40_v40_v32(8, out0, out1, seqOut)` |
| `_vnot_v32_v32(oop, vin, vout)` | Vector NOT | `_vnot_v32_v32(oop_8op, vMsbMask, viNotMsbMask)` |

**Files:** `GeneratePbchDmRs.cpp`, `GenerateGoldSeq.cpp`, `LogicalAntennaPortUtilsVect.hpp`

---

## Vector Pack/Unpack Operations

### Pack Operations

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vpack64_v32_v32_dwl(mdw, vin, vout, offset)` | Pack 64-bit to 32-bit | `_vpack64_v32_v32_dwl(mdw_4dw, viSum, viRes, 0)` |
| `_vpack_v32_v32_bl(oop, vin, vout, offset)` | Pack byte low | `_vpack_v32_v32_bl(oop_4op, vNoiseBitsW, vNoiseBitsBytes, 0)` |

### Unpack Operations

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vunpack40_v40_v32_dwl(mdw, vin, offset, vout)` | Unpack 40-bit double-word low | `_vunpack40_v40_v32_dwl(mdw_4dw, voMult, 0, viSum0)` |
| `_vunpack32_v32_v32_dwl(mdw, vin, offset, vout)` | Unpack 32-bit double-word low | `_vunpack32_v32_v32_dwl(mdw_4dw, vin, 0, v1)` |
| `_vunpackl_v32_v32_w_u(oop, vin, offset, vout)` | Unpack low word unsigned | `_vunpackl_v32_v32_w_u(oop_4op, vIn, 0, vIn)` |

**Files:** `CalculateCorrShortAntDmrs.cpp`, `UpdateNoiseNlExp.hpp`, `FloatingPointUtils.hpp`

---

## Vector Clear and Fill Operations

### Clear Operations

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vclr_v32(oop, vout)` | Clear 32-bit vector | `_vclr_v32(8, vIn)` |
| `_vclr_v40(oop, vout)` | Clear 40-bit vector | `_vclr_v40(8, vOut1)` |
| `_vclr_v32_declaration(count, oop, vout)` | Clear with declaration | `_vclr_v32_declaration(1, mdw_8dw, viIn0)` |
| `_vclr_v40_declaration(count, oop, vout)` | Clear 40-bit with declaration | `_vclr_v40_declaration(1, mdw_8dw, viSum)` |
| `_vclr_c32_1op(c)` | Clear scalar | `_vclr_c32_1op(vcrA)` |

### Fill Operations

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vfill_c32_v32_dw(oop, c, vout)` | Fill vector with scalar | `_vfill_c32_v32_dw(8, vc0Tmp, vi0CoefPlus)` |
| `_vfill_c32_v40_dw(oop, c, vout)` | Fill 40-bit vector with scalar | `_vfill_c32_v40_dw(8, b_ssC, precVec)` |
| `_vfill_imm8_3_v32_dw(oop, imm, vout)` | Fill with 8-bit immediate | `_vfill_imm8_3_v32_dw(8, 1, pssVec)` |
| `_vfill_c32_v32_dw_declaration(count, oop, c, vout)` | Fill with declaration | `_vfill_c32_v32_dw_declaration(1, 8, vcConst, vFract)` |
| `_vfillw_c32_v32(oop, c, vout)` | Fill word vector | `_vfillw_c32_v32(8, cScale, vScale)` |
| `_vfillw_imm8_3_v32(oop, imm, vout)` | Fill word with immediate | `_vfillw_imm8_3_v32(oop_8op, 0, vLayer0)` |

**Files:** `CalculateCorrShortAntDmrs.cpp`, `NrDlJob.cpp`, `PrepareSymbol.cpp`, `GeneratePssAlg.cpp`

---

## Vector Special Operations

### Min/Max Operations

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vmaxint_v32_c32_v32(mdw, vin, c, low/high, vout)` | Max integer with scalar | `_vmaxint_v32_c32_v32(mdw_4dw, viExp, vcMax, LOW, viMaxExp0)` |
| `_vminintw_v32_c32_v32(oop, vin, c, vout)` | Min integer word | `_vminintw_v32_c32_v32(8, vData, cMin, vOut)` |

### Exponent Operations

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vexp32_v32_v32_w(oop, va, vb, vout, offset)` | 32-bit exponent | `_vexp32_v32_v32_w(OOP, inA, inB, outZ, offsetZ)` |
| `_vexp32_v32_v32_w_uns_3p(oop, vin, vout, offset)` | Unsigned exponent 3-param | `_vexp32_v32_v32_w_uns_3p(oop_8op, vNoisePower, vBit, 0)` |

### Bit Operations

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vbpc_v32_v32_v32_v32_v32_v32_vi(s, h1, h2, h3, h4, vout)` | Bit parity check | `_vbpc_v32_v32_v32_v32_v32_v32_vi(s, H1, H2, H3, H4, out0)` |
| `_vbpermute_v32_v32_v32_clr_4p(vin, vperm, off1, vout, off2)` | Bit permute | `_vbpermute_v32_v32_v32_clr_4p(vin, vperm, 0, vout, 0)` |
| `_vbtranspose_v32_v32_w(va, vout)` | Bit transpose word | `_vbtranspose_v32_v32_w(vA, vZ)` |

### Vector Move

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vmovw_v32_v32(oop, vin, offin, vout, offout)` | Move word vector | `_vmovw_v32_v32(8, vi0CoefPlus, 0, viModSeq, 0)` |
| `_vmovw_v32_v32_p(oop, vin, offin, vout, offout, vpr)` | Predicated move | `_vmovw_v32_v32_p(8, vi1CoefMinus, 0, viModSeq, 0, vprPseudoRandSeq)` |
| `_vvmov_v40_v32_vuX(vcu, vin, vout)` | Move between VCUs | `_vvmov_v40_v32_vuX(VCU1, viRes, viRes1)` |

### Transpose

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vtransw_v32_v32_uimm3_v32_2w_Nop(oop, va, vb, imm, vout)` | Transpose word 2-way | `_vtransw_v32_v32_uimm3_v32_2w_Nop(oop_4op, vLayer0, vLayer1, 0, vOut0)` |
| `_vpermutew_v32_v32_v32_clr(oop, vcfg, vin, vtemp, vout)` | Permute word with clear | `_vpermutew_v32_v32_v32_clr(16, H1, s, H4, out0)` |

### Absolute Value

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vabs16_v32_v32(oop, vin, vout)` | 16-bit absolute value | `_vabs16_v32_v32(8, vData, vOut)` |
| `_vabs32_v32_v32(oop, vin, vout)` | 32-bit absolute value | `_vabs32_v32_v32(8, vData, vOut)` |

### Square Root

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vsqrt_v32_v32_v32(oop, vin, vout1, vout2)` | Vector square root | `_vsqrt_v32_v32_v32(8, vData, vRes, vTemp)` |
| `_vsqrti_v32_v32_v32(oop, vin, vout1, vout2)` | Vector inverse square root | `_vsqrti_v32_v32_v32(8, vData, vInvRes, vTemp)` |

**Files:** `CalculateCorrShortAntDmrs.cpp`, `RimRsMapperAlg.cpp`, `GenerateGoldSeq.cpp`, `LogicalAntennaPortUtilsVect.hpp`, `CalculateRddMatrixCommon.hpp`

---

## Bit Field Configuration Operations

These intrinsics configure DSP hardware registers for vector operations.

### Saturation Mode

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_lbfv_uimm4_vsatmod(val)` | Load bit field saturation mode | `_lbfv_uimm4_vsatmod(0xf)` |
| `_lbfv_uimm4_vsatmode(val)` | Load bit field saturation mode | `_lbfv_uimm4_vsatmode(0xD)` |

**Values:**
- `0x0`: All saturation enabled
- `0xf`: All saturation disabled
- `0xD`: Specific saturation pattern

### Vector Position Shift (VPS)

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vlbf_uimm5_vps0(val)` | Load VPS0 shift value | `_vlbf_uimm5_vps0(0x3)` |
| `_vlbf_uimm5_vps1(val)` | Load VPS1 shift value | `_vlbf_uimm5_vps1(0x0)` |
| `_lbfv_uimm5_vps1(val)` | Load VPS1 shift value | `_lbfv_uimm5_vps1(4)` |

**Values:**
- `0x0`: No shift
- `0x1`: Left shift by 1
- `0x2`: Left shift by 2
- `0x3`: Left shift by 3

### Multiplication Sign Mode (MSN)

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vlbf_uimm2_vmsn0(val)` | Load MSN0 multiplication sign | `_vlbf_uimm2_vmsn0(0x3)` |
| `_lbfv_uimm2_vmsn0(val)` | Load MSN0 multiplication sign | `_lbfv_uimm2_vmsn0(0)` |
| `_vlbf_uimm2_vmsn1(val)` | Load MSN1 multiplication sign | `_vlbf_uimm2_vmsn1(0x0)` |
| `_lbfv_uimm2_vmsn1(val)` | Load MSN1 multiplication sign | `_lbfv_uimm2_vmsn1(0)` |

**Values:**
- `0x0`: Both unsigned
- `0x3`: Both signed

### Rounding Control

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vlbf_uimm1_vrnda(val)` | Load rounding mode | `_vlbf_uimm1_vrnda(0x1)` |
| `_vlbf_uimm1_vrndv(val)` | Load vector rounding | `_vlbf_uimm1_vrndv(1)` |
| `_lbfv_uimm1_vrndv2w(val)` | Load vector 2-word rounding | `_lbfv_uimm1_vrndv2w(1)` |
| `_vlbf_uimm1_vrndlv(val)` | Load long vector rounding | `_vlbf_uimm1_vrndlv(1)` |

**Values:**
- `0`: Rounding disabled
- `1`: Rounding enabled

### Shift Mode

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_lbfv_uimm2_vshfw(val)` | Load shift word mode | `_lbfv_uimm2_vshfw(2)` |
| `_vlbf_uimm1_vshfd(val)` | Load shift double mode | `_vlbf_uimm1_vshfd(0)` |
| `_vlbf_uimm2_vshfdw(val)` | Load shift double-word | `_vlbf_uimm2_vshfdw(2)` |
| `_vlbf_uimm2_vshfl(val)` | Load shift low | `_vlbf_uimm2_vshfl(0)` |

### Division/Square Root Exponent

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vlbf_uimm5_vdivexpb(val)` | Load division exponent base | `_vlbf_uimm5_vdivexpb(25)` |
| `_lbfv_uimm5_vsqrtexpb(val)` | Load square root exponent base | `_lbfv_uimm5_vsqrtexpb(25)` |
| `_vlbf_uimm5_vsqrtiexpb(val)` | Load inverse sqrt exponent base | `_vlbf_uimm5_vsqrtiexpb(25)` |

**Values:**
- `16`: Default value
- `25`: Extended precision

### Other Configuration

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vlbf_uimm3_voop(val)` | Load vector operation mode | `_vlbf_uimm3_voop(1)` |
| `_lbf_uimm3_vux(val)` | Load bit field VUX | `_lbf_uimm3_vux(inA)` |

**Files:** `GenerateDmrs.cpp`, `FillRegistersAndDmemWithConstValues.cpp`, `PrepareSymbol.cpp`, `ScaleCQ.cpp`

---

## Mode Register Operations

### MODV0 Register (Mode Vector 0)

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vmova_a0_modv0(val)` | Load MODV0 register | `_vmova_a0_modv0(0xE0D)` |
| `_vmova_a8_modv0(val)` | Load MODV0 via A8 | `_vmova_a8_modv0(originalModv0)` |

**Common Values:**
- `0xE0D`: Standard saturation/shift configuration
- `0xE0F`: VPS0 shift disabled
- `0x1F000EAF`: Extended configuration

### MODV2 Register (Mode Vector 2)

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vmova_a0_modv2(val)` | Load MODV2 register | `_vmova_a0_modv2(0xE06000)` |
| `_vmova_a8_modv2(val)` | Load MODV2 via A8 | `_vmova_a8_modv2(originalModv2)` |

**Common Values:**
- `0xE06000`: Standard VPS1/VMSN1 configuration
- `0x606000`: Alternative configuration

### MODV Configuration Helpers

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vmova_a16_c32_1op_declaration(count, val, c)` | Declare MODV operand | `_vmova_a16_c32_1op_declaration(1, deltaSum, vcTmp1)` |
| `_vmovi_imm32_6_c32_declaration(count, val, c)` | Declare immediate coef | `_vmovi_imm32_6_c32_declaration(1, -9, vcTmp2)` |
| `_vmovi_imm32_6_v32_vuX(vcu, val, v, count)` | Move immediate to VCU | `_vmovi_imm32_6_v32_vuX(0, 0x80000001, s, 1)` |

**Files:** `CalculateCorrShortAntDmrs.cpp`, `GenericModvSaver.hpp`, `AntCorrUtils.hpp`

---

## Floating Point Operations

### Floating Point Multiply

| Intrinsic | Description | Example Usage |
|-----------|-------------|---------------|
| `_vflpmpy_v32_v32_v32(oop, va, vb, vout)` | Floating point multiply | `_vflpmpy_v32_v32_v32(8, vIn, vFract, vIn)` |

**Files:** `VecFlp2Int.cpp`, `LogarithmMacros.hpp`

---

## Common Usage Patterns

### Typical Initialization Sequence

```cpp
// Save original mode registers
uint32_t originalModv0 = _vmova_a0_modv0(0xE0D);
uint32_t originalModv2 = _vmova_a8_modv2(0xE06000);

// Configure bit fields
_lbfv_uimm4_vsatmod(0xf);     // Disable saturation
_vlbf_uimm5_vps0(0x3);         // Left shift by 3
_vlbf_uimm2_vmsn0(0x3);        // Signed × signed
_vlbf_uimm1_vrnda(0x1);        // Enable rounding

// Declare and initialize vectors
_vclr_v32_declaration(1, mdw_8dw, vData);
_vlddw_c32_clone_1dw(&scale, cScale);
_vfill_c32_v32_dw(8, cScale, vScaleVec);

// Perform operations
_vlddw_v32(mdw_8dw, input, vIn, 0);
_vmpyxp_v32_v32_v32(8, vIn, 0, vScaleVec, 0, vOut);
_vstdw_v32(mdw_8dw, vOut, 0, output);

// Restore original mode registers
_vmova_a0_modv0(originalModv0);
_vmova_a8_modv2(originalModv2);
```

### Complex Signal Processing Example

```cpp
// Initialize for complex multiplication
_vmova_a0_modv0(0xE0D);
_vlbf_uimm5_vps0(0x3);         // Shift left by 3
_vlbf_uimm2_vmsn0(0x3);        // Signed multiplication

// Load complex data
_vlddw_v32(mdw_8dw, chanEstHrs0, viIn0, 0);
_vlddw_v32(mdw_8dw, chanEstHrs1, viIn1, 0);

// Complex MAC operation
_vgenmac3_v32_v32_v40(mdw_6dw, viCfg, viIn0, viIn1, voMult, voMult);

// Accumulate results
_vunpack40_v40_v32_dwl(mdw_4dw, voMult, 0, viSum0);
_vadd64_v32_v32_v32(mdw_4dw, viSum, viSum0, viSum);
```

---

## Declaration Variants

Most intrinsics have a `_declaration` variant that combines variable declaration with initialization:

- **Standard:** `_vlddw_v32(mdw_8dw, src, vOut, 0);` (requires `vec_t vOut;` before)
- **Declaration:** `_vlddw_v32_declaration(1, mdw_8dw, src, vOut, 0);` (declares `vOut`)

The first parameter `(1)` indicates the variable count.

---

## Predication Variants

Many intrinsics support predicated execution with `_p` suffix:

```cpp
// Load predicate register
_vlddw_vpr_dw(&vcuSeq, vpr0);

// Conditional move based on predicate
_vmovw_v32_v32(8, vDataA, 0, vOut, 0);              // Unconditional
_vmovw_v32_v32_p(8, vDataB, 0, vOut, 0, vpr0);      // Where vpr0 is true
```

---

## Operand Naming Conventions

- **`oop`**: Operand count (e.g., `mdw_8dw` = 8 double-words)
- **`mdw_Xdw`**: Multi-double-word width (X = 1, 2, 4, 6, 8)
- **`LOW` / `HIGH`**: Word selection for 16-bit operations
- **`VCU0` / `VCU1`**: Vector Computation Unit selection
- **`VMPS0` / `VMPS1`**: Vector Multiply Position Shift register

---

## Performance Considerations

1. **Memory Alignment:** All vector loads/stores should be aligned to 32-byte boundaries for optimal performance.
2. **Loop Unrolling:** Use `PRAGMA_CEVA_UNROLL(1)` to prevent compiler unrolling when manual optimization is applied.
3. **VPR Usage:** Predicated operations avoid conditional branches, improving pipeline efficiency.
4. **MODV Configuration:** Configure MODV registers once at function entry, restore on exit.
5. **VCU Parallelism:** Use both VCU0 and VCU1 when possible to double throughput.

---

## References

**Primary Source Files:**
- `app/dsp/nr/ul/pusch/alg/thor/CalculateCorrShortAntDmrs.cpp`
- `app/dsp/nr/dl/common/alg/CsiRsMapperAlg.cpp`
- `app/dsp/nr/dl/common/alg/RimRsMapperAlg.cpp`
- `app/dsp/nr/common/alg/ScaleCQ.cpp`
- `app/dsp/common/alg/FrequencyOffsetIntraSymbolAlgMultiUe.hpp`
- `app/dsp/common/LogarithmMacros.hpp`
- `app/dsp/common/utils/GenericModvSaver.hpp`

**Total Intrinsics Cataloged:** 200+

---

*Document generated: January 2026*  
*Project: l1sw - Physical Layer (L1) Software for LTE/NR on CEVA DSP*
