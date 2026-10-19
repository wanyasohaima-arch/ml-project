export type Feature = {
  name: string;
  label: string;
  kind: 'number' | 'category';
  required: boolean;
  options?: string[];
  min?: number;
  max?: number;
};

export const FEATURES: Feature[] = [
  { name: 'race', label: 'Race', kind: 'category', required: true,
    options: ['Caucasian', 'AfricanAmerican', 'Hispanic', 'Asian', 'Other', 'Unknown'] },
  { name: 'gender', label: 'Gender', kind: 'category', required: true,
    options: ['Female', 'Male'] },
  { name: 'age', label: 'Age group', kind: 'category', required: true,
    options: ['[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', '[50-60)',
              '[60-70)', '[70-80)', '[80-90)', '[90-100)'] },
  { name: 'A1Cresult', label: 'A1C result (Unknown = not measured)', kind: 'category',
    required: true, options: ['Unknown', 'Norm', '>7', '>8'] },
  { name: 'insulin', label: 'Insulin', kind: 'category', required: true,
    options: ['No', 'Steady', 'Up', 'Down'] },
  { name: 'change', label: 'Medication change (No / Ch)', kind: 'category', required: true,
    options: ['No', 'Ch'] },
  { name: 'diabetesMed', label: 'Diabetes medication', kind: 'category', required: true,
    options: ['No', 'Yes'] },
  { name: 'time_in_hospital', label: 'Days in hospital', kind: 'number', required: true, min: 1, max: 14 },
  { name: 'num_lab_procedures', label: 'Lab procedures', kind: 'number', required: true, min: 0, max: 140 },
  { name: 'num_procedures', label: 'Procedures', kind: 'number', required: true, min: 0, max: 10 },
  { name: 'num_medications', label: 'Medications', kind: 'number', required: true, min: 0, max: 100 },
  { name: 'number_outpatient', label: 'Outpatient visits', kind: 'number', required: true, min: 0, max: 100 },
  { name: 'number_emergency', label: 'Emergency visits', kind: 'number', required: true, min: 0, max: 100 },
  { name: 'number_inpatient', label: 'Inpatient visits', kind: 'number', required: true, min: 0, max: 100 },
  { name: 'number_diagnoses', label: 'Number of diagnoses', kind: 'number', required: true, min: 1, max: 20 },
];