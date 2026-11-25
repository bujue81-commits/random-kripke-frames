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

def toE1 (i : Fin 3) : Fin 1 := 0

theorem F1001_to_T2 :
    IsBoundedMorphism F1001 T2 collapse1001 := by
  refine ⟨?_, ?_, ?_⟩
  · intro y
    fin_cases y
    · exact ⟨0, by simp [collapse1001]⟩
    · exact ⟨1, by simp [collapse1001]⟩
  · intro x y h
    simp [T2]
  · intro x z h
    fin_cases z
    · exact ⟨0, by simp [F1001, collapse1001]⟩
    · exact ⟨1, by simp [F1001, collapse1001]⟩

theorem F0001_to_E1 :
    IsBoundedMorphism F0001 E1 toE1 := by
  refine ⟨?_, ?_, ?_⟩
  · intro y
    exact ⟨0, by simp [toE1]⟩
  · intro x y h
    simp [E1]
  · intro x z h
    fin_cases z
    fin_cases x <;> exact ⟨0, by simp [F0001, toE1]⟩

theorem F1001_to_E1 :
    IsBoundedMorphism F1001 E1 toE1 := by
  refine ⟨?_, ?_, ?_⟩
  · intro y
    exact ⟨0, by simp [toE1]⟩
  · intro x y h
    simp [E1]
  · intro x z h
    fin_cases z
    fin_cases x <;> exact ⟨0, by simp [F1001, toE1]⟩

end RandomKripke