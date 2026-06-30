---
name: ceva-dsp-programming
description: Use when user asks about CEVA DSP programming, CEVA intrinsics, CEVA Vec-C intrinsics, CEVA kernel optimization, CEVA SIMD implementation, CEVA mode bits, vectorPack/vectorShift/vectorExponent style operations, complex or semi-complex CEVA operations, or asks to analyze, explain, implement, or optimize a CEVA DSP kernel function.
license:
---

Use this skill for CEVA DSP kernel development, intrinsics selection, and optimization work in L1SW.

## Scope

- Target architecture: CEVA-XC22 / XC6
- Main codebase area: `app/dsp/`
- Common use cases:
	- explain what a CEVA intrinsic does
	- explain CEVA Vec-C naming or intrinsic families
	- choose intrinsics for a kernel or hot loop
	- optimize CEVA SIMD code
	- map an algorithm to CEVA vector operations
	- answer mode-bit or configuration-register questions
	- route vector, complex, semi-complex, or width-specific CEVA operations to the right reference file
	- analyze an existing CEVA DSP kernel in L1SW

## Working Rules

- Do not load the entire `reference/` directory.
- Do not load `reference/README.md` unless the task is broad category discovery.
- First inspect the user request and the relevant code.
- Then read only the minimum number of reference files needed for the task.
- Prefer reference files whose names directly match the operation or intrinsic family in the request.
- If the request names a specific intrinsic or operation, load that exact reference file first.
- If the request contains a filename-like operation name, map it to the exact reference filename before using any broader category routing.
- Normalize user wording when matching filenames: ignore case, and treat spaces, hyphens, and underscores as interchangeable.
- If the request is about an existing kernel, search the code in `app/dsp/` first, then load only the matching reference docs.

## Recommended Workflow

### Existing kernel analysis

1. Read the user request carefully and identify the operation family.
2. Inspect the relevant CEVA code in the workspace, usually under `app/dsp/`.
3. Map any filename-like request terms to exact reference filenames.
4. Load only the most relevant reference file or files from `ceva-dsp-programming/reference/`.
5. If needed, load one summary file for cross-checking:
	 - `reference/quick-reference.md`
	 - `reference/CEVA_DSP_Intrinsics_Summary.md`
6. Provide the answer or implementation using intrinsics that already appear in the L1SW codebase when possible.

### Greenfield intrinsic selection

1. Read the user request carefully and identify the operation family.
2. Map any filename-like request terms to exact reference filenames.
3. Load the smallest matching reference file set.
4. Search `app/dsp/` for similar intrinsics usage before recommending a final choice.
5. If needed, load one summary file for cross-checking.

## Exact Filename Routing

Prefer exact filenames over category routing whenever the request is specific enough.

- `vector pack 72 bits` -> `reference/vectorPack72-bits.md`
- `vector shift 72 bit` -> `reference/vectorShift72-bit.md`
- `vector exponent long 72 bit` -> `reference/vectorExponentLong72-bit.md`
- `semi complex 32x16` -> `reference/semi-complex32x16.md`
- `semi complex 32x16 with exponent` -> `reference/semi-complex32x16WithExponent.md`
- `complex 32x16` -> `reference/complex32x16.md`
- `load predicate` -> `reference/loadPredicate.md`
- `store predicate register` -> `reference/storePredicateRegister.md`

When both a generic file and a vector-specific file seem applicable:

- prefer the `vector*` file for vector-form questions
- prefer the width-specific file for `40-bit`, `64-bit`, or `72-bit` questions
- prefer the `WithExponent` variant when the request explicitly mentions exponent handling

## Routing Guide

Use the smallest matching set of files.

### By operation family

- Load and store:
	- `reference/load.md`
	- `reference/store.md`
	- `reference/loadPredicate.md`
	- `reference/storePredicateRegister.md`
- Arithmetic:
	- `reference/addition.md`
	- `reference/subtract.md`
	- `reference/absolute.md`
	- `reference/negate.md`
	- `reference/round.md`
- Multiply and MAC:
	- `reference/multiply.md`
	- `reference/multiply-accumulate.md`
	- `reference/multiply-subtract.md`
	- `reference/genericMultiply.md`
	- `reference/genericMultiply-accumulate.md`
- Shift, scale, exponent:
	- `reference/shift.md`
	- `reference/scale.md`
	- `reference/exponent.md`
	- `reference/normalize.md`
- Compare, predicate, masking:
	- `reference/compare.md`
	- `reference/predicateRegisterManipulation.md`
	- `reference/and.md`
	- `reference/or.md`
	- `reference/xor.md`
- Pack, unpack, transpose, permute:
	- `reference/pack.md`
	- `reference/unpack.md`
	- `reference/transpose.md`
	- `reference/permute.md`
- Floating point:
	- `reference/floatArithmetic.md`
	- `reference/floatMultiplication.md`
	- `reference/floatDivision.md`
	- `reference/floatNormalize.md`

### By data shape or complex form

- `16x16`, `32x16`, `32x32` patterns:
	- `reference/16x16.md`
	- `reference/32x16.md`
	- `reference/32x32.md`
- Complex:
	- `reference/complex16x16.md`
	- `reference/complex32x16.md`
	- `reference/complex32x32.md`
- Semi-complex:
	- `reference/semi-complex16x16.md`
	- `reference/semi-complex16x32.md`
	- `reference/semi-complex32x16.md`
	- `reference/semi-complex32x32.md`
- With exponent handling:
	- load the matching `WithExponent` reference file

### By mode-register and configuration questions

- Saturation, rounding, overflow, multiplication mode bits:
	- `reference/saturationModeBits.md`
	- `reference/roundingModeBits.md`
	- `reference/overflowModeBits.md`
	- `reference/multiplicationModeBits.md`
- Division, floating-point, store pre-shift, automatic mode bits:
	- `reference/divisionModeBits.md`
	- `reference/floatingPointModeBits.md`
	- `reference/storePre-shiftModeBits.md`
	- `reference/automicOperationsModeBits.md`

## L1SW-Specific Guidance

- Prefer intrinsics that are already used in L1SW, especially under `app/dsp/`.
- When suggesting an optimization, preserve the kernel's numerical intent, scaling, and saturation behavior.
- Check whether the implementation depends on:
	- vector width and lane layout
	- Q-format or exponent tracking
	- VCU0 and VCU1 split
	- MODV0, MODV2, and related mode bits
	- load and store alignment and post-modify addressing
- Do not recommend generic CEVA intrinsics blindly if there is no evidence they are used or supported in this codebase.

## Answer Expectations

- Explain why a chosen intrinsic fits the operand shape and data flow.
- Call out scaling, rounding, overflow, and accumulator width when relevant.
- For optimization tasks, compare the new approach against the current kernel structure.
- For implementation tasks, prefer minimal, verifiable changes.

## Fallbacks

- If the exact intrinsic is unknown, search the workspace for similar usage before proposing one.
- If multiple reference files may apply, read the most specific file first and only then add a broader summary file.
- If the request is broad, use `reference/README.md` only as an index, not as the primary source.