import RandomKripke.FiniteFrames

namespace RandomKripke

/-- Equality of successor images, in proposition form, is exactly forth and back. -/
theorem boundedMorphism_iff_successorImages
    {α β : Type} (R : Frame α) (S : Frame β) (f : α → β) :
    IsBoundedMorphism R S f ↔
      Function.Surjective f ∧
        (∀ x z, S (f x) z = true ↔ ∃ y, R x y = true ∧ f y = z) := by
  constructor
  · intro h
    refine ⟨h.1, ?_⟩
    intro x z
    constructor
    · exact h.2.2 x z
    · rintro ⟨y, hy, hfy⟩
      rw [← hfy]
      exact h.2.1 x y hy
  · rintro ⟨hs, hh⟩
    refine ⟨hs, ?_, ?_⟩
    · intro x y hy
      exact (hh x (f y)).2 ⟨y, hy, rfl⟩
    · intro x z hz
      exact (hh x z).1 hz

/-- Four-point central frame, with bit 8 coding (1,1) and bit 0 coding (3,3). -/
def central4Frame (n : Fin 512) : Frame (Fin 4) := fun i j =>
  if i.val = 0 ∨ j.val = 0 then true
  else decide ((n.val / 2 ^ (8 - (3 * (i.val - 1) + (j.val - 1)))) % 2 = 1)

/-- Encode the peripheral relation in row-major, most-significant-bit-first order. -/
def encodeCentral4 (R : Frame (Fin 4)) : Nat :=
  (if R 1 1 then 256 else 0) +
  (if R 1 2 then 128 else 0) +
  (if R 1 3 then 64 else 0) +
  (if R 2 1 then 32 else 0) +
  (if R 2 2 then 16 else 0) +
  (if R 2 3 then 8 else 0) +
  (if R 3 1 then 4 else 0) +
  (if R 3 2 then 2 else 0) +
  (if R 3 3 then 1 else 0)

/-- All six peripheral permutations, as lists of images of 0,1,2,3. -/
def censusPermutations4 : List (Fin 4 → Fin 4) :=
  [![0,1,2,3], ![0,1,3,2], ![0,2,1,3],
   ![0,2,3,1], ![0,3,1,2], ![0,3,2,1]]

def relabelCentral4 (n : Fin 512) (p : Fin 4 → Fin 4) : Nat :=
  encodeCentral4 (fun i j => central4Frame n (p i) (p j))

def canonicalCentral4 (n : Fin 512) : Nat :=
  (censusPermutations4.map (relabelCentral4 n)).foldl Nat.min n.val

def canonicalCentral4Codes : Finset (Fin 512) :=
  Finset.univ.filter (fun n => canonicalCentral4 n = n.val)

/-- Exact finite encoding/decoding check. -/
theorem census4_encoding_roundtrip :
    ∀ n : Fin 512, encodeCentral4 (central4Frame n) = n.val := by
  native_decide

theorem census4_central :
    ∀ (n : Fin 512) (i : Fin 4),
      central4Frame n 0 i = true ∧ central4Frame n i 0 = true := by
  native_decide

/-- Finite count of the representatives for the six stated permutations. -/
theorem census4_canonical_count : canonicalCentral4Codes.card = 104 := by
  native_decide

/-- Two-point minimal target: all arrows except the peripheral loop. -/
def censusK2 : Frame (Fin 2) := fun i j =>
  decide (i.val = 0 ∨ j.val = 0)

def hasSmallerMinimalImage4 (n : Fin 512) : Prop :=
  (∃ f : Fin 4 → Fin 2, IsBoundedMorphism (central4Frame n) censusK2 f) ∨
  (∃ f : Fin 4 → Fin 3, IsBoundedMorphism (central4Frame n) F0001 f) ∨
  (∃ f : Fin 4 → Fin 3, IsBoundedMorphism (central4Frame n) F1001 f)

instance (n : Fin 512) : Decidable (hasSmallerMinimalImage4 n) := by
  unfold hasSmallerMinimalImage4
  infer_instance

def inheritedCentral4Codes : Finset (Fin 512) :=
  canonicalCentral4Codes.filter hasSmallerMinimalImage4

/-- This is a count of quotient structures, not a probability theorem. -/
theorem census4_smaller_image_count : inheritedCentral4Codes.card = 70 := by
  native_decide

/-- Lists of classifications from the hand probability proofs.
    Here only finite combinatorial properties of the lists are checked. -/
def manuscriptMinimal4 : Finset (Fin 512) :=
  {20, 21, 28, 29, 73, 82, 83, 89, 93, 98, 99, 105, 107, 113, 115, 121, 211, 214, 285, 309, 311, 371}

def manuscriptPositive4 : Finset (Fin 512) :=
  {91, 123, 215, 219, 221, 223, 319, 347, 375, 381, 383, 511}

theorem census4_minimal_list_count : manuscriptMinimal4.card = 22 := by
  native_decide

theorem census4_positive_list_count : manuscriptPositive4.card = 12 := by
  native_decide

/-- The listed types partition the canonical representatives, using the
    actual bounded-morphism predicate for the inherited class. -/
theorem census4_list_partition :
    ∀ n : Fin 512,
      n ∈ canonicalCentral4Codes ↔
        n ∈ inheritedCentral4Codes ∨ n ∈ manuscriptMinimal4 ∨
          n ∈ manuscriptPositive4 := by
  native_decide

theorem census4_lists_disjoint :
    ∀ n : Fin 512,
      (n ∈ manuscriptMinimal4 → n ∉ manuscriptPositive4) ∧
      (n ∈ manuscriptMinimal4 → ¬ hasSmallerMinimalImage4 n) ∧
      (n ∈ manuscriptPositive4 → ¬ hasSmallerMinimalImage4 n) := by
  native_decide

/-- A certificate encodes a canonical source, target index (0=K2,
    1=F0001, 2=F1001), and four map digits in base 2 or 3. -/
structure Census4Certificate where
  source : Fin 512
  target : Fin 3
  digits : Nat

def censusMap2 (n : Nat) (i : Fin 4) : Fin 2 :=
  ⟨(n / 2 ^ (3 - i.val)) % 2, Nat.mod_lt _ (by decide)⟩

def censusMap3 (n : Nat) (i : Fin 4) : Fin 3 :=
  ⟨(n / 3 ^ (3 - i.val)) % 3, Nat.mod_lt _ (by decide)⟩

def census4CertificateValid (c : Census4Certificate) : Bool :=
  if c.target.val = 0 then
    decide (IsBoundedMorphism (central4Frame c.source) censusK2 (censusMap2 c.digits))
  else if c.target.val = 1 then
    decide (IsBoundedMorphism (central4Frame c.source) F0001 (censusMap3 c.digits))
  else
    decide (IsBoundedMorphism (central4Frame c.source) F1001 (censusMap3 c.digits))

/-- Reflection of each Boolean certificate check to the existing Prop. -/
theorem census4Certificate_sound (c : Census4Certificate)
    (h : census4CertificateValid c = true) :
    hasSmallerMinimalImage4 c.source := by
  unfold census4CertificateValid at h
  unfold hasSmallerMinimalImage4
  split at h
  · exact Or.inl ⟨censusMap2 c.digits, of_decide_eq_true h⟩
  · split at h
    · exact Or.inr (Or.inl ⟨censusMap3 c.digits, of_decide_eq_true h⟩)
    · exact Or.inr (Or.inr ⟨censusMap3 c.digits, of_decide_eq_true h⟩)

def manuscriptCertificates4 : List Census4Certificate :=
  [
    ⟨0, 0, 7⟩,
    ⟨1, 1, 14⟩,
    ⟨2, 0, 6⟩,
    ⟨3, 0, 6⟩,
    ⟨6, 0, 6⟩,
    ⟨7, 0, 6⟩,
    ⟨9, 1, 17⟩,
    ⟨10, 0, 6⟩,
    ⟨11, 0, 6⟩,
    ⟨12, 0, 6⟩,
    ⟨13, 0, 6⟩,
    ⟨14, 0, 6⟩,
    ⟨15, 0, 6⟩,
    ⟨17, 1, 17⟩,
    ⟨19, 1, 17⟩,
    ⟨22, 1, 15⟩,
    ⟨23, 1, 15⟩,
    ⟨27, 1, 17⟩,
    ⟨30, 1, 15⟩,
    ⟨31, 1, 15⟩,
    ⟨36, 0, 4⟩,
    ⟨37, 0, 4⟩,
    ⟨38, 0, 4⟩,
    ⟨39, 0, 4⟩,
    ⟨45, 0, 4⟩,
    ⟨46, 0, 4⟩,
    ⟨47, 0, 4⟩,
    ⟨53, 0, 4⟩,
    ⟨55, 0, 4⟩,
    ⟨63, 0, 4⟩,
    ⟨74, 0, 6⟩,
    ⟨75, 0, 6⟩,
    ⟨78, 0, 6⟩,
    ⟨79, 0, 6⟩,
    ⟨81, 2, 16⟩,
    ⟨84, 2, 16⟩,
    ⟨85, 2, 16⟩,
    ⟨86, 1, 15⟩,
    ⟨87, 1, 15⟩,
    ⟨90, 0, 1⟩,
    ⟨92, 0, 1⟩,
    ⟨94, 0, 1⟩,
    ⟨95, 1, 15⟩,
    ⟨102, 0, 4⟩,
    ⟨103, 0, 4⟩,
    ⟨108, 0, 4⟩,
    ⟨109, 0, 4⟩,
    ⟨110, 0, 4⟩,
    ⟨111, 0, 4⟩,
    ⟨117, 0, 4⟩,
    ⟨118, 0, 4⟩,
    ⟨119, 0, 4⟩,
    ⟨124, 0, 4⟩,
    ⟨125, 0, 4⟩,
    ⟨126, 0, 4⟩,
    ⟨127, 0, 4⟩,
    ⟨209, 2, 7⟩,
    ⟨213, 2, 7⟩,
    ⟨222, 0, 1⟩,
    ⟨238, 0, 4⟩,
    ⟨239, 0, 4⟩,
    ⟨245, 0, 4⟩,
    ⟨247, 0, 4⟩,
    ⟨255, 0, 4⟩,
    ⟨273, 2, 22⟩,
    ⟨275, 2, 22⟩,
    ⟨279, 2, 21⟩,
    ⟨283, 2, 22⟩,
    ⟨287, 2, 21⟩,
    ⟨351, 2, 21⟩
  ]

theorem census4_certificate_count : manuscriptCertificates4.length = 70 := by
  decide

/-- Every explicit CSV map satisfies actual forth, back, and surjectivity. -/
theorem census4_all_certificates_valid :
    manuscriptCertificates4.all census4CertificateValid = true := by
  native_decide

def certificateCentral4Codes : Finset (Fin 512) :=
  (manuscriptCertificates4.map Census4Certificate.source).toFinset

/-- The explicit maps cover exactly the independently enumerated inherited class. -/
theorem census4_certificate_coverage :
    certificateCentral4Codes = inheritedCentral4Codes := by
  native_decide

end RandomKripke
