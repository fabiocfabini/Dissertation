## Intruduction
- [x] Intro -- cross section, luminosity, event
- [x] The Large Hadron Collider -- Emphasis on experiment environment IP
  - [x] The Cern Accelerator Complex: Experiments, Filling Scheme)
  - [x] Accelerator Sequence (Emphasis on bunch creation for background on GS analysis: RF Buckets, Bunch Anatomy)
- [ ] The CMS Experiment
  - [ ] Luminometers
      - [ ] Anatomy
      - [ ] Position at LHC
      - [ ] Observables
  - [ ] DCCT and FBCT
  - [ ] Beam Position Monotoring (Mention for background on ROD implementation for DIAG scans)

## Luminosity
- [ ] Definition
  - [ ] Instantaneous/Integrated Luminosity
    - [ ] Formulas
    - [ ] Their relevance to the experiment:
      - [ ] Detector performance (instantaneous)
      - [ ] Beam adjustment (instantaneous)
      - [ ] Other experiments results (instantaneous/Integrated) (needed? mention this in introduction)
- [ ] Luminosity from Machine Parameters
  - [ ] Mention of complicated collision environment in hadron colliders
  - [ ] Need for calculating Luminosity without cross section knowledge
  - [ ] Derivation from Beam/Machine Paremeters
- [ ] Zero Counting Method

## The Van der Meer Method
- [] Van der Meer Scan
- [] Van der Meer Program
  - [] Conditions during the program
  - [] Scans Performed

## Corrections to Luminosity
- [ ] Mention all moving parts (To help guide the reader on why applying the corrections is of importance)
  - [ ] Make (possibly) usefull distinction between corrections applied in the framework and outside the framework? (Calibration vs Integration corrections?)
- [ ] Framework Corrections (Calibration)
  - [ ] Background (This is the odd one since it is not really detector agnostic)
  - [ ] FBCT to DCCT calibration
  - [ ] GS correction
  - [ ] Orbit Drift
  - [ ] Lenght Scale
  - [ ] Beam effects
  - [ ] XY Factorization
  - [ ] Peak correction
- [ ] Efficiency & Linearity Correction (Integration)
  - [ ] Mention equation ``L = e*L + a*L**2``
  - [ ] Explain efficiency factor `e`. What it tries to correct.
  - [ ] Explain (non-)linearity factor `a`. What it tries to correct.

## Display of 2023 Results
    **TBD**

## VdMFramework
- [ ] It's purpose
- [ ] How it works
  - [ ] Thinking of making a flow diagram of the framework. (Could also be usefull for documentation and aid a possible future rewrite)
- [ ] My contributions:
  - [ ] Implementation of ROD correction to Diagonal scans
  - [ ] Performance improvements:
    - [ ] Discuss problem
    - [ ] Present proposed solution
    - [ ] Show benchmarks

# vdM Tools, H2B (possibly other)
- TBD