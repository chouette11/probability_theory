import random
from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

def energy(mol):
    """ 分子のエネルギーを計算する関数 """
    ff = AllChem.UFFGetMoleculeForceField(mol)
    print(ff.CalcEnergy())
    return ff.CalcEnergy()

def perturb_structure(mol, temperature):
    """ 温度に依存したランダムな構造変更を行う関数 """
    conf = mol.GetConformer()
    for i in range(mol.GetNumAtoms()):
        # 各原子に対して小さな変位を加える
        pos = conf.GetAtomPosition(i)
        displacement = np.random.normal(0, 0.1 * temperature, 3)
        conf.SetAtomPosition(i, pos + displacement)
    return mol

def simulated_annealing(mol, initial_temp, final_temp, alpha):
    """ 焼きなまし法による分子構造最適化 """
    temp = initial_temp
    current_mol = Chem.Mol(mol)
    current_energy = energy(current_mol)

    while temp > final_temp:
        new_mol = Chem.Mol(current_mol)
        new_mol = perturb_structure(new_mol, temp)
        new_energy = energy(new_mol)
        # エネルギーが下がった場合は常に採用
        # エネルギーが上がった場合は一定確率で採用
        if new_energy < current_energy or random.random() < np.exp((current_energy - new_energy) / temp):
            current_mol = new_mol
            current_energy = new_energy
        temp *= alpha  # 温度を減少

    return current_mol

# SDF ファイルから分子を読み込む
sdf_filename = "MA.sdf"
sdf_supplier = Chem.SDMolSupplier(sdf_filename)
cyclohexane = sdf_supplier[0]  # 最初の分子を読み込む
AllChem.EmbedMolecule(cyclohexane, randomSeed=42)

# 焼きなまし法のパラメータ
initial_temp = 100000
final_temp = 0.1
alpha = 0.95

# 最適化
optimized_mol = simulated_annealing(cyclohexane, initial_temp, final_temp, alpha)

# 最適化された構造のエネルギー
optimized_energy = energy(optimized_mol)
print(f"Optimized Energy: {optimized_energy}")

# 結果を保存
writer = Chem.SDWriter(f'optimized_cyclohexane_{optimized_energy}_{initial_temp}_{final_temp}_{alpha}.sdf')
writer.write(optimized_mol)
writer.close()
