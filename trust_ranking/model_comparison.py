import matplotlib.pyplot as plt

model1_a= new_data_nested = [
    [0.0496, 0.0524, 0.0542, 0.0556, 0.0555, 0.0588, 0.0851, 0.0615, 0.0605, 0.0630, 0.0635, 0.0652, 0.0647, 0.0642, 0.0640, 0.0661],
    [0.5590, 0.5815, 0.5974, 0.6141, 0.6121, 0.6501, 0.6606, 0.6718, 0.6727, 0.6930, 0.6936, 0.7107, 0.6976, 0.7023, 0.7104, 0.7223],
    [0.4205, 0.4275, 0.4666, 0.4995, 0.5292, 0.5636, 0.5712, 0.5844, 0.5912, 0.5967, 0.6061, 0.6125, 0.6056, 0.5961, 0.6277, 0.6253],
    [0.4966, 0.5076, 0.5433, 0.5723, 0.5949, 0.6298, 0.6360, 0.6501, 0.6550, 0.6655, 0.6721, 0.6806, 0.6719, 0.6658, 0.6908, 0.6927]
]

model2_a=[[
    0.0384, 0.0447, 0.0463, 0.0471, 0.0473, 0.0459, 0.0471, 0.0475, 0.0455, 0.0470,
    0.0476, 0.0460, 0.0488, 0.0476, 0.0468, 0.0475
],[
    0.4304, 0.4955, 0.5112, 0.5280, 0.5202, 0.5112, 0.5189, 0.5403, 0.5127, 0.5349,
    0.5317, 0.5223, 0.5440, 0.5230, 0.5203, 0.5258
],[
    0.4106, 0.4215, 0.4169, 0.4192, 0.4189, 0.4252, 0.4268, 0.4305, 0.4284, 0.4249,
    0.4187, 0.4256, 0.4217, 0.4248, 0.4232, 0.4237
],[
    0.4590, 0.4825, 0.4828, 0.4894, 0.4859, 0.4898, 0.4917, 0.5003, 0.4933, 0.4947,
    0.4888, 0.4932, 0.4950, 0.4917, 0.4912, 0.4917
]]


model3_a=[[
    0.0186, 0.0266, 0.0371, 0.0335, 0.0394, 0.0452, 0.0426, 0.0409, 
    0.0430, 0.0415, 0.0424, 0.0459, 0.0432, 0.0423, 0.0428, 0.0446
],[
    0.2630, 0.3330, 0.4341, 0.3941, 0.4456, 0.5006, 0.4787, 0.4629, 
    0.4957, 0.4712, 0.4783, 0.5013, 0.4831, 0.4783, 0.4832, 0.4944
],[
    0.1913, 0.3931, 0.4031, 0.4126, 0.4168, 0.4271, 0.421, 0.4197, 
    0.4320, 0.4273, 0.4151, 0.4193, 0.4143, 0.4223, 0.4172, 0.4004
],[
    0.2376, 0.4142, 0.4537, 0.4498, 0.467, 0.4878, 0.4793, 0.4729, 
    0.4934, 0.4828, 0.5508, 0.4828, 0.4751, 0.4798, 0.4762, 0.4667
]]

model1_c=[
    [0.0730, 0.0753, 0.0793, 0.0805, 0.0822, 0.0851, 0.0859, 0.0883, 0.0893, 0.0906, 0.0902, 0.0930, 0.092, 0.0909, 0.0894, 0.0903],
    [0.6237, 0.6458, 0.6852, 0.6913, 0.7113, 0.7252, 0.7446, 0.7545, 0.7695, 0.7702, 0.7780, 0.7979, 0.7903, 0.7857, 0.7739, 0.7791],
    [0.4348, 0.4611, 0.4967, 0.5475, 0.5630, 0.6150, 0.6422, 0.6459, 0.6546, 0.6555, 0.6606, 0.6654, 0.6706, 0.6587, 0.6781, 0.6745],
    [0.5557, 0.5788, 0.6167, 0.6538, 0.6705, 0.7105, 0.7345, 0.7382, 0.7499, 0.7491, 0.7552, 0.7626, 0.7637, 0.7541, 0.7674, 0.7654]
]


model2_c=[[
    0.0742, 0.0740, 0.0744, 0.0746, 0.0741, 0.0753, 0.0745, 0.0754, 0.0745, 0.0749,
    0.0740, 0.0730, 0.0741, 0.0734, 0.0724, 0.0738
],[
    0.6327, 0.6348, 0.6388, 0.6345, 0.6348, 0.6420, 0.6302, 0.6454, 0.6319, 0.6403,
    0.6241, 0.6249, 0.6315, 0.6327, 0.6216, 0.6305
],[
    0.4338, 0.4274, 0.4332, 0.4292, 0.4270, 0.4261, 0.4248, 0.4274, 0.4264, 0.4307,
    0.4313, 0.4320, 0.4303, 0.4402, 0.4394, 0.4477
],[
    0.5552, 0.5510, 0.5553, 0.5527, 0.5513, 0.5521, 0.5483, 0.5530, 0.5503, 0.5544,
    0.5520, 0.5523, 0.5524, 0.5618, 0.5570, 0.5664
]]

model3_c=[[
    0.0506, 0.0744, 0.0739, 0.0743, 0.0744, 0.0735, 0.0740, 0.0743,
    0.0731, 0.0726, 0.0741, 0.0746, 0.0736, 0.0721, 0.0738, 0.0735
],[
    0.4466, 0.6314, 0.6351, 0.6307, 0.6358, 0.6216, 0.6315, 0.6323,
    0.6232, 0.6177, 0.6276, 0.6377, 0.6337, 0.6188, 0.6296, 0.6327
],[
    0.4618, 0.4320, 0.4351, 0.4283, 0.4296, 0.4246, 0.4220, 0.4246,
    0.4309, 0.4378, 0.4292, 0.4269, 0.4319, 0.4396, 0.4364, 0.4331
],[
    0.5327, 0.5537, 0.5580, 0.5509, 0.5538, 0.5456, 0.5469, 0.5491,
    0.5506, 0.5557, 0.4754, 0.5519, 0.5542, 0.5563, 0.5557, 0.5553
]]

# plt.plot(model1_a[0], label='Model without Differential Privacy')
# plt.plot(model2_a[0], label='Model with Differential Privacy of Epsilon 0.5')
# plt.plot(model3_a[0], label='Model with Differential Privacy of Epsilon 1.0')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.title('Loss comparision between Models of API recommendation')
# plt.legend()
# plt.show()

# plt.plot(model1_c[0], label='Model without Differential Privacy')
# plt.plot(model2_c[0], label='Model with Differential Privacy of Epsilon 0.5')
# plt.plot(model3_c[0], label='Model with Differential Privacy of Epsilon 1.0')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.title('Loss comparision between Models of Category recommendation')
# plt.legend()
# plt.show()

plt.plot(model1_a[0], label='Model without Differential Privacy')
plt.plot(model2_a[0], label='Model with Differential Privacy of Epsilon 0.5')
plt.plot(model3_a[0], label='Model with Differential Privacy of Epsilon 1.0')
plt.xlabel('Epoch')
plt.ylabel('Precision')
plt.title('Precision comparision between Models of API recommendation')
plt.legend()
plt.show()

plt.plot(model1_c[0], label='Model without Differential Privacy')
plt.plot(model2_c[0], label='Model with Differential Privacy of Epsilon 0.5')
plt.plot(model3_c[0], label='Model with Differential Privacy of Epsilon 1.0')
plt.xlabel('Epoch')
plt.ylabel('Precision')
plt.title('Precision comparision between Models of Category recommendation')
plt.legend()
plt.show()

plt.plot(model1_a[1], label='Model without Differential Privacy')
plt.plot(model2_a[1], label='Model with Differential Privacy of Epsilon 0.5')
plt.plot(model3_a[1], label='Model with Differential Privacy of Epsilon 1.0')
plt.xlabel('Epoch')
plt.ylabel('Recall')
plt.title('Recall comparision between Models of API recommendation')
plt.legend()
plt.show()

plt.plot(model1_c[1], label='Model without Differential Privacy')
plt.plot(model2_c[1], label='Model with Differential Privacy of Epsilon 0.5')
plt.plot(model3_c[1], label='Model with Differential Privacy of Epsilon 1.0')
plt.xlabel('Epoch')
plt.ylabel('Recall')
plt.title('Recall comparision between Models of Category recommendation')
plt.legend()
plt.show()

plt.plot(model1_a[2], label='Model without Differential Privacy')
plt.plot(model2_a[2], label='Model with Differential Privacy of Epsilon 0.5')
plt.plot(model3_a[2], label='Model with Differential Privacy of Epsilon 1.0')
plt.xlabel('Epoch')
plt.ylabel('Average Precision')
plt.title('Average Precision comparision between Models of API recommendation')
plt.legend()
plt.show()

plt.plot(model1_c[2], label='Model without Differential Privacy')
plt.plot(model2_c[2], label='Model with Differential Privacy of Epsilon 0.5')
plt.plot(model3_c[2], label='Model with Differential Privacy of Epsilon 1.0')
plt.xlabel('Epoch')
plt.ylabel('Average Precision')
plt.title('Average Precision comparision between Models of Category recommendation')
plt.legend()
plt.show()


plt.plot(model1_a[3], label='Model without Differential Privacy')
plt.plot(model2_a[3], label='Model with Differential Privacy of Epsilon 0.5')
plt.plot(model3_a[3], label='Model with Differential Privacy of Epsilon 1.0')
plt.xlabel('Epoch')
plt.ylabel('NDCG')
plt.title('NDCG comparision between Models of API recommendation')
plt.legend()
plt.show()

plt.plot(model1_c[3], label='Model without Differential Privacy')
plt.plot(model2_c[3], label='Model with Differential Privacy of Epsilon 0.5')
plt.plot(model3_c[3], label='Model with Differential Privacy of Epsilon 1.0')
plt.xlabel('Epoch')
plt.ylabel('NDCG')
plt.title('NDCG comparision between Models of Category recommendation')
plt.legend()
plt.show()

