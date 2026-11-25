import Mathlib

namespace RandomKripke

/-- A directed Kripke frame, with loops allowed. -/
abbrev Frame (W : Type) := W → W → Bool

/-- A surjective bounded morphism of directed frames. -/
def IsBoundedMorphism {α β : Type}
    (R : Frame α) (S : Frame β) (f : α → β) : Prop :=
  Function.Surjective f ∧
    (∀ x y, R x y = true → S (f x) (f y) = true) ∧
    (∀ x z, S (f x) z = true →
      ∃ y, R x y = true ∧ f y = z)

/-- Surjectivity is decidable between finite types. -/
instance instDecidableSurjective {α β : Type}
    [Fintype α] [Fintype β] [DecidableEq β] (f : α → β) :
    Decidable (Function.Surjective f) := by
  unfold Function.Surjective
  infer_instance

/-- Bounded morphism conditions are decidable on finite frames. -/
instance instDecidableBoundedMorphism {α β : Type}
    [Fintype α] [Fintype β] [DecidableEq β]
    (R : Frame α) (S : Frame β) (f : α → β) :
    Decidable (IsBoundedMorphism R S f) := by
  unfold IsBoundedMorphism
  infer_instance

/-- The frame coded 0001, in the order (c,a,b). -/
def F0001 : Frame (Fin 3) := fun i j =>
  if i.val = 0 then true
  else if i.val = 1 then decide (j.val = 0)
  else decide (j.val = 0 ∨ j.val = 2)

/-- The frame coded 1001, in the order (c,a,b). -/
def F1001 : Frame (Fin 3) := fun i j =>
  if i.val = 0 then true
  else if i.val = 1 then decide (j.val = 0 ∨ j.val = 1)
  else decide (j.val = 0 ∨ j.val = 2)

/-- Complete reflexive frame on two points. -/
def T2 : Frame (Fin 2) := fun _ _ => true

/-- Reflexive singleton frame. -/
def E1 : Frame (Fin 1) := fun _ _ => true

def HasCentralPoint {α : Type} (R : Frame α) : Prop :=
  ∃ c, ∀ x, R c x = true ∧ R x c = true

def IsSerial {α : Type} (R : Frame α) : Prop :=
  ∀ x, ∃ y, R x y = true


/-- A nonempty frame maps onto the reflexive singleton exactly when it is serial. -/
theorem boundedMorphism_to_E1_iff_serial
    {α : Type} [Nonempty α] (R : Frame α) :
    IsBoundedMorphism R E1 (fun _ : α => (0 : Fin 1)) ↔ IsSerial R := by
  constructor
  · intro h x
    obtain ⟨y, hxy, hy⟩ := h.2.2 x 0 (by simp [E1])
    exact ⟨y, hxy⟩
  · intro hs
    refine ⟨?_, ?_, ?_⟩
    · intro z
      exact ⟨Classical.choice ‹Nonempty α›, Subsingleton.elim _ _⟩
    · intro x y hxy
      simp [E1]
    · intro x z hz
      obtain ⟨y, hxy⟩ := hs x
      exact ⟨y, hxy, Subsingleton.elim _ _⟩

/-- A map onto T2 is bounded precisely when every source point
    reaches every target fibre. The forth condition is automatic. -/
theorem boundedMorphism_to_T2_iff
    {α : Type} (R : Frame α) (f : α → Fin 2) :
    IsBoundedMorphism R T2 f ↔
      Function.Surjective f ∧
        (∀ x z, ∃ y, R x y = true ∧ f y = z) := by
  constructor
  · intro h
    refine ⟨h.1, ?_⟩
    intro x z
    exact h.2.2 x z (by simp [T2])
  · rintro ⟨hs, hhit⟩
    refine ⟨hs, ?_, ?_⟩
    · intro x y hxy
      simp [T2]
    · intro x z hz
      exact hhit x z

theorem F0001_central : HasCentralPoint F0001 := by
  refine ⟨0, ?_⟩
  intro x
  fin_cases x <;> decide

theorem F1001_central : HasCentralPoint F1001 := by
  refine ⟨0, ?_⟩
  intro x
  fin_cases x <;> decide

theorem F0001_serial : IsSerial F0001 := by
  intro x
  fin_cases x <;> decide

theorem F1001_serial : IsSerial F1001 := by
  intro x
  fin_cases x <;> decide

def collapse1001 (i : Fin 3) : Fin 2 :=
  if i.val = 0 then 0 else 1

def toE1 (_i : Fin 3) : Fin 1 := 0

def swap2 (i : Fin 2) : Fin 2 :=
  if i.val = 0 then 1 else 0

/-- Up to swapping the two target labels, the only
    surjective bounded morphism from F1001 onto a two-point
    frame has fibre partition {c} | {a,b}. -/
theorem F1001_two_point_maps_are_canonical :
    ∀ (f : Fin 3 → Fin 2),
      IsBoundedMorphism F1001 T2 f →
        f = collapse1001 ∨ f = swap2 ∘ collapse1001 := by
  decide


/-- Bounded morphisms compose. -/
theorem boundedMorphism_comp
    {α β γ : Type}
    {R : Frame α} {S : Frame β} {T : Frame γ}
    {f : α → β} {g : β → γ}
    (hf : IsBoundedMorphism R S f)
    (hg : IsBoundedMorphism S T g) :
    IsBoundedMorphism R T (g ∘ f) := by
  rcases hf with ⟨hfs, hff, hfb⟩
  rcases hg with ⟨hgs, hgf, hgb⟩
  refine ⟨?_, ?_, ?_⟩
  · intro z
    obtain ⟨y, hy⟩ := hgs z
    obtain ⟨x, hx⟩ := hfs y
    exact ⟨x, by simpa [Function.comp, hx] using hy⟩
  · intro x y hxy
    exact hgf (f x) (f y) (hff x y hxy)
  · intro x z hxz
    obtain ⟨z', hz', hzcomp⟩ := hgb (f x) z hxz
    obtain ⟨y, hxy, hycomp⟩ := hfb x z' hz'
    exact ⟨y, hxy, by
      simpa [Function.comp, hycomp] using hzcomp⟩

theorem F1001_to_T2 :
    IsBoundedMorphism F1001 T2 collapse1001 := by
  decide

/-- Exhaustive finite classification: F0001 has no two-point
    surjective bounded-morphic image. -/
theorem F0001_no_two_point_quotient :
    ¬ ∃ (S : Frame (Fin 2)) (f : Fin 3 → Fin 2),
      IsBoundedMorphism F0001 S f := by
  decide

/-- Every two-point bounded-morphic image of F1001 is T2. -/
theorem F1001_two_point_quotient_target :
    ∀ (S : Frame (Fin 2)) (f : Fin 3 → Fin 2),
      IsBoundedMorphism F1001 S f → S = T2 := by
  decide


theorem F0001_to_E1 :
    IsBoundedMorphism F0001 E1 toE1 := by
  decide

theorem F1001_to_E1 :
    IsBoundedMorphism F1001 E1 toE1 := by
  decide

end RandomKripke